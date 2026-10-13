export async function getUserClient(): Promise<{
  id: string;
  email: string;
  username?: string;
} | null> {
  try {
    // Same-origin request; next.config.ts rewrites it to the Django API.
    // A timeout keeps the nav bar from waiting forever if the API is slow or down.
    const res = await fetch("/api/auth/user", {
      credentials: "include",
      signal: AbortSignal.timeout(8000),
    });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}
