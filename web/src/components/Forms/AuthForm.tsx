import { ReactNode } from "react"

interface AuthFormProps {
  children: ReactNode
}

export default function AuthForm({ children }: AuthFormProps) {
  return (
    <form className="pt-8 w-full max-w-sm mx-auto flex flex-col gap-2 items-center ">
      {children}
    </form>
  )
}
