export async function getUserClient(): Promise<{
  id: string;
  email: string;
  username?: string;
} | null> {
  try {
    // Same-origin request; next.config.ts rewrites it to the Django API.
    const res = await fetch("/api/auth/user", { credentials: "include" });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}
