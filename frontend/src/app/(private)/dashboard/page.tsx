import { cookies } from "next/headers";

export default async function DashboardPage() {
  const cookieStore = await cookies();
  const cookie = cookieStore.get("sessionid");

  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <p className="text-muted-foreground mt-2">
        Welcome to your protected dashboard. Your session cookie is:
      </p>
      <pre className="bg-muted text-muted-foreground rounded-md p-4 mt-4">
        {cookie?.value || "No session cookie"}
      </pre>
    </div>
  );
}
