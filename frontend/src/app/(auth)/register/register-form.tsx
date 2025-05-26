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


export const registerSchema = z
.object({
email: z.string().email("Invalid email address"),
password: z.string().min(6, "Password must be at least 6 characters"),
confirmPassword: z.string().min(6, "Confirm your password"),
})
.refine((data) => data.password === data.confirmPassword, {
message: "Passwords do not match",
path: ["confirmPassword"],
});

export function RegisterForm() {
const form = useAppForm({
defaultValues: {
email: "",
password: "",
confirmPassword: "",
},
validatorAdapter: zodValidator,
validators: {
onSubmit: registerSchema,
onChange: registerSchema,
},
onSubmit: async ({ value }) => {
console.log("Registering", value);
},
});

return (
<Card className="max-w-sm mx-auto mt-12">
    <CardHeader>
        <CardTitle className="text-xl">Register</CardTitle>
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


            <form.AppField name="confirmPassword">
                {(field) => (<div>
                    <field.TextField label="Confirm Password" type="password" />
                </div>)}
            </form.AppField>

            <form.AppForm>
                <form.SubmitButton>Register</form.SubmitButton>
            </form.AppForm>
        </form>
    </CardContent>

    <CardFooter className="flex flex-col gap-4">
        <div className="w-full border-t pt-4 text-center text-sm text-muted-foreground">OR</div>
        <SocialLoginButtons />
        <p className="text-sm text-center">
            Already have an account?{" "}
            <Link href="/login" className="text-blue-600 hover:underline">
            Sign in
            </Link>
        </p>
    </CardFooter>
</Card>
);
}
