export async function getUserClient(): Promise<{
  id: string;
  email: string;
  username?: string;
} | null> {
  try {
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/auth/user/`, {
      credentials: "include",
    });

    if (!res.ok) {
      console.warn("===== User fetch failed", res.status);
      return null;
    }

    console.log("===== User fetch success", res.status);
    return await res.json();
  } catch (err) {
    console.error("===== User fetch exception:", err);
    return null;
  }
}
