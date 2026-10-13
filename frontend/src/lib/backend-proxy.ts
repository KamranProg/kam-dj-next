import { NextResponse, type NextRequest } from "next/server";

/**
 * Forward an auth POST to the Django API on behalf of the browser.
 *
 * Django's CSRF cookie is HttpOnly, so client code cannot read it. This runs
 * on the server, where the cookie can be copied into the X-CSRFToken header.
 * The Origin header is forwarded because Django requires it (or a Referer)
 * to pass its CSRF check over HTTPS.
 */
export async function forwardToBackend(req: NextRequest, backendPath: string) {
  const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;

  const upstream = await fetch(`${backendUrl}${backendPath}`, {
    method: "POST",
    cache: "no-store",
    headers: {
      "Content-Type": "application/json",
      Cookie: req.headers.get("cookie") ?? "",
      "X-CSRFToken": req.cookies.get("csrftoken")?.value ?? "",
      Origin: req.headers.get("origin") ?? req.nextUrl.origin,
    },
    body: await req.text(),
  });

  // Django answers 204 No Content on success when no API token is issued.
  const data = upstream.status === 204 ? {} : await upstream.json().catch(() => ({}));
  const response = NextResponse.json(data, {
    status: upstream.status === 204 ? 200 : upstream.status,
  });

  // Pass every Set-Cookie (sessionid, csrftoken, ...) on to the browser.
  for (const cookie of upstream.headers.getSetCookie()) {
    response.headers.append("set-cookie", cookie);
  }

  return response;
}
