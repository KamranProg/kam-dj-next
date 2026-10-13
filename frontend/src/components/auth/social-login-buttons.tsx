"use client";

import { FaGoogle, FaFacebookF } from "react-icons/fa";
import { Button } from "@/components/ui/button";

export function SocialLoginButtons() {
  return (
    <div className="flex flex-col gap-2 w-full">
      <Button variant="outline" className="w-full" onClick={() => alert("Sign in with Google")}>
        <FaGoogle className="mr-2" /> Sign in with Google
      </Button>
      <Button variant="outline" className="w-full" onClick={() => alert("Sign in with Facebook")}>
        <FaFacebookF className="mr-2" /> Sign in with Facebook
      </Button>
    </div>
  );
}
