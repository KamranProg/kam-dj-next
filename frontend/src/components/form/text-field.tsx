import { useFieldContext } from '@/components/form/index.tsx';
import { Input } from "@/components/ui/input";
import { FieldErrors } from '@/components/form/field-errors.tsx';

type TextFieldProps = {
label: string;
} & React.InputHTMLAttributes<HTMLInputElement>;
    export function TextField({ label, ...inputProps }: TextFieldProps) {
    const field = useFieldContext<string>();


        return (
        <div>
            <Input id={field.name} placeholder={label} value={field.state.value} onChange={(e)=> field.handleChange(e.target.value)}
            // onBlur={field.handleBlur}
            {...inputProps}
            />
            <FieldErrors meta={field.state.meta} />
        </div>
        )
        }
