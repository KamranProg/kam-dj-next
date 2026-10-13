export default function AboutPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 py-10">
      <h1 className="text-3xl font-bold mb-4">About</h1>
      <p className="text-muted-foreground">
        This app demonstrates registration, login and logout with Django sessions, a protected
        dashboard, and a Next.js layer that keeps the CSRF handling on the server.
      </p>
    </div>
  );
}
