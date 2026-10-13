import { z } from "zod";
import { passwordRules } from "@/app/(auth)/register/schema";

export const loginSchema = z.object({
  email: z.string().email("Invalid email address"),
  password: passwordRules,
});

export type LoginFormValues = z.infer<typeof loginSchema>;

export type LoginFormBody = LoginFormValues & { username: string };
