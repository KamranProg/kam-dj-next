export default function Home() {
  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-4">Authentication starter</h1>
      <p className="text-muted-foreground">
        A Next.js frontend talking to a Django REST API with cookie-based sessions and CSRF
        protection. Create an account or sign in to reach the protected dashboard.
      </p>
    </div>
  );
}
