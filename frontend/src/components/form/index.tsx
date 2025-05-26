import { createFormHookContexts, createFormHook } from '@tanstack/react-form'
import { TextField } from '@/components/form/text-field'
import { SubmitButton } from '@/components/form/submit-button'
// export useFieldContext for use in your custom components
export const { fieldContext, useFieldContext, formContext, useFormContext } =
  createFormHookContexts();


export const { useAppForm } = createFormHook({
  fieldContext,
  formContext,
  // We'll learn more about these options later
  fieldComponents: {
    TextField
  },
  formComponents: {
    SubmitButton
  },
})