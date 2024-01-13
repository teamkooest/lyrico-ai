import { useState, ChangeEvent } from "react"

/** Framer Motion */
import { motion, AnimatePresence } from "framer-motion"

/** Componens */
import AuthForm from "../components/Forms/AuthForm"
import Inputs from "../components/Inputs/Input"
import Button from "../components/Buttons/Button"

export default function Auth() {
  /** States */
  const [, setEmailValue] = useState("")
  const [showLoginForm, setShowLoginForm] = useState(true)
  const [showRegistrationForm, setShowRegistrationForm] = useState(false)

  /** Toggles */
  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
    setEmailValue(event.target.value)
  }

  const onSubmit = () => {
    console.log('Submitted.')
  }

  const toggleForms = () => {
    setShowLoginForm((prev) => !prev)
    setShowRegistrationForm((prev) => !prev)
  }

  return (
    <div className="w-full h-full">
      <div className="flex flex-col items-center justify-center w-full h-full">
        <div className="p-8 w-full max-w-xs flex flex-col gap-4 items-center">
          <AnimatePresence>
            { showLoginForm && (
              <motion.div
                key="loginForm"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.3 }}
                className="flex flex-col items-center text-white text-center"
              >
                <div className="flex flex-col items-center text-white text-center">
                  <h1 className="text-4xl font-medium text-center">
                    vocale ai.
                  </h1>
                  <span className="pt-4 text-sm font-medium">Hey, enter your details to get signed in into your account.</span>
                </div>
                <AuthForm>
                  <Inputs id="email" placeholder="Enter Email" type="email" value="" onChange={onChange} />
                  <Inputs id="password" placeholder="Password" type="password" value="" onChange={() => {}} />
                  <Button label="Sign in" type="submit" onClick={onSubmit} className="mt-4" />
                </AuthForm>
              </motion.div>
            )}
          </AnimatePresence>
          <AnimatePresence>
            { showRegistrationForm && (
              <motion.div
                key="registrationForm"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                transition={{ duration: 0.3 }}
                className="flex flex-col items-center text-white text-center"
              >
                <div className="flex flex-col items-center text-white text-center">
                  <h1 className="text-4xl font-medium text-center">
                    vocale ai.
                  </h1>
                  <span className="pt-4 text-sm font-medium">Hey, welcome aboard. Wanna create magical lyrics?</span>
                </div>
                <AuthForm>
                  <Inputs id="email" placeholder="Enter Email" type="email" value="" onChange={onChange} />
                  <Inputs id="password" placeholder="Password" type="password" value="" onChange={() => {}} />
                  <Inputs id="password" placeholder="Retype Password" type="password" value="" onChange={() => {}} />
                  <Button label="Sign up" type="submit" onClick={onSubmit} className="mt-4" />
                </AuthForm>
              </motion.div>
            )}
          </AnimatePresence>

          <div className="text-white text-sm mt-4">
            {showLoginForm ? "Don't have an account?" : "Already have an account?"}
            <button onClick={toggleForms} className="text-indigo-500 ml-1 focus:outline-none">
              {showLoginForm ? "Register now" : "Sign in"}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
