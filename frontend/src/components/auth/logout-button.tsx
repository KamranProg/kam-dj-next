"use client";

import { useTransition } from "react";
import { useRouter } from "next/navigation";
import { toast } from "sonner";
import { Button } from "@/components/ui/button";
import { useAuth } from "@/context/auth-context";
import type { ApiResponseStatus } from "@/types/api";

async function logoutViaProxy(): Promise<ApiResponseStatus> {
  try {
    const res = await fetch("/api/proxy/auth/logout/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      credentials: "include",
    });

    if (!res.ok) {
      return {
        status: "error",
        message: "Logout failed",
      };
    }

    return {
      status: "success",
      message: "Logged out",
    };
  } catch (err) {
    console.error("Logout error:", err);
    return {
      status: "error",
      message: "Unexpected error",
    };
  }
}

export function LogoutButton() {
  const router = useRouter();
  const [isPending, startTransition] = useTransition();
  const { refreshUser } = useAuth();

  async function handleLogout() {
    const result = await logoutViaProxy();

    if (result.status === "error") {
      toast.error(result.message);
      return;
    }

    await refreshUser();

    toast.success(result.message);

    startTransition(() => {
      router.refresh();
      router.push("/login");
    });
  }

  return (
    <Button variant="ghost" onClick={handleLogout} disabled={isPending}>
      {isPending ? "Logging out..." : "Logout"}
    </Button>
  );
}
