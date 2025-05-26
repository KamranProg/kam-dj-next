import { useStore } from "@tanstack/react-form";
import { useFormContext } from ".";
import { Button } from "@/components/ui/button";

type SubmitButtonProps = {
  children: React.ReactNode;
};

export const SubmitButton = ({ children }: SubmitButtonProps) => {
  const form = useFormContext();

  const [isSubmitting, isValid, isTouched] = useStore(form.store, (state) => [
    state.isSubmitting,
    state.isValid,
    state.isTouched,
  ]);

  const isDisabled = isSubmitting || !isTouched || !isValid;

  return (
    <Button type="submit" disabled={isDisabled} className="w-full">
      {children}
    </Button>
  );
};
