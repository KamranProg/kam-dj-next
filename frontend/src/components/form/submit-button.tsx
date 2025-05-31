import { useStore } from "@tanstack/react-form";
import { Button } from "@/components/ui/button";
import { useFormContext } from ".";

type SubmitButtonProps = {
  children: React.ReactNode;
  isPending?: boolean;
};

export const SubmitButton = ({ children, isPending }: SubmitButtonProps) => {
  const form = useFormContext();

  const [isSubmitting, isValid, isTouched, canSubmit] = useStore(form.store, (state) => [
    state.isSubmitting,
    state.isValid,
    state.isTouched,
    state.canSubmit
  ]);

  const isDisabled = isPending || isSubmitting || !isTouched || !isValid || !canSubmit;

  return (
    <Button type="submit" disabled={isDisabled} className="w-full">
      {children}
    </Button>
  );
};
