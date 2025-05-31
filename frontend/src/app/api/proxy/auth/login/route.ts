import { cookies } from "next/headers";
import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const cookieStore = cookies();
  const cookieHeader = cookieStore.toString();
  const csrfToken = cookieStore.get("csrftoken")?.value ?? "";

  const body = await req.json();

  const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/auth/login/`, {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      Cookie: cookieHeader,
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify(body),
  });

  const data = await res.json().catch(() => ({}));

  // Forward Set-Cookie headers from Django to the browser
  const proxyRes = NextResponse.json(
    data?.message ? { message: data.message } : data,
    { status: res.status }
  );
  const setCookie = res.headers.get("set-cookie");
  if (setCookie) {
    proxyRes.headers.set("set-cookie", setCookie);
  }

  return proxyRes;
}
