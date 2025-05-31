import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/auth/logout/`, {
    method: "POST",
    headers: {
      cookie: req.headers.get("cookie") || "",
      "Content-Type": "application/json",
      "X-CSRFToken": req.cookies.get("csrftoken")?.value || "",
    },
    credentials: "include",
  });

  return new NextResponse(null, { status: res.status });
}
