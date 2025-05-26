"use client";

import { z } from "zod";
import { zodValidator } from "@tanstack/zod-form-adapter";
import Link from "next/link";

import {
Card,
CardHeader,
CardTitle,
CardContent,
CardFooter,
} from "@/components/ui/card";
import { SocialLoginButtons } from "../social-login-buttons";
import { useAppForm } from "@/components/form";

export const loginSchema = z.object({
email: z.string().email("Invalid email address"),
password: z.string().min(6, "Password must be at least 6 characters"),
});

export function LoginForm() {
const form = useAppForm({
defaultValues: {
email: "",
password: "",
},
validatorAdapter: zodValidator,
validators: {
onSubmit: loginSchema,
onChange: loginSchema,
},
onSubmit: async ({ value }) => {
console.log("Login submit", value);
},
});

return (
<Card className="max-w-sm mx-auto mt-12">
    <CardHeader>
        <CardTitle className="text-xl">Login</CardTitle>
    </CardHeader>
    <CardContent>
        <form onSubmit={form.handleSubmit} className="space-y-4">
            <form.AppField name="email">
                {(field) => (<div>
                    <field.TextField label="Email" type="email" />
                </div>)}
            </form.AppField>

            <form.AppField name="password">
                {(field) => (<div>
                    <field.TextField label="Password" type="password" />
                </div>)}
            </form.AppField>

            <div className="text-right">
                <Link href="/forgot-password" className="text-sm text-blue-600 hover:underline">
                Forgot your password?
                </Link>
            </div>

            <form.AppForm>
                <form.SubmitButton>Sign in</form.SubmitButton>
            </form.AppForm>
        </form>
    </CardContent>

    <CardFooter className="flex flex-col gap-4">
        <div className="w-full border-t pt-4 text-center text-sm text-muted-foreground">OR</div>
        <SocialLoginButtons />
        <p className="text-sm text-center">
            Don&apos;t have an account?{" "}
            <Link href="/register" className="text-blue-600 hover:underline">
            Register
            </Link>
        </p>
    </CardFooter>
</Card>
);
}
