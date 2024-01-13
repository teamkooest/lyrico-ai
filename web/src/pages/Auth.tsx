import { useState, ChangeEvent, startTransition } from "react";

/** React Router DOM */
import { useNavigate } from "react-router-dom";

/** Components */
import Logo from "../components/Logos/Logo";
import AuthForm from "../components/Forms/AuthForm";
import Inputs from "../components/Inputs/Input";
import Button from "../components/Buttons/Button";

export default function Auth() {

  const navigate = useNavigate();

  /** States */
  const [emailValue, setEmailValue] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showLoginForm, setShowLoginForm] = useState(true);

  /** Toggles */
  const onChange = (event: ChangeEvent<HTMLInputElement>) => {
    setEmailValue(event.target.value);
  };

  const onPasswordChange = (event: ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const onConfirmPasswordChange = (event: ChangeEvent<HTMLInputElement>) => {
    setConfirmPassword(event.target.value);
  };

  const onSubmit = () => {
    console.log("Submitted.");
    if (showLoginForm) {
      console.log("Login Password:", password);
    } else {
      console.log("Registration Password:", password);
      console.log("Confirm Password:", confirmPassword);
    }

    startTransition(() => {
      navigate("/chat");
    });
  };

  const toggleForms = () => {
    setShowLoginForm((prev) => !prev);
  };

  return (
    <div className="w-full h-full">
      <div className="flex flex-col items-center justify-center w-full h-full">
        <div className="p-8 w-full max-w-xs flex flex-col gap-4 items-center">
          <div>
            <div className="flex flex-col items-center text-white text-center">
              <Logo />
              {showLoginForm ? (
                <p className="pt-4 text-sm font-medium">
                  Hey, welcome to <span className="text-indigo-500 font-bold">vocale ai</span>. Enter your details to get started.
                </p>
              ) : (
                <p className="pt-4 text-sm font-medium">
                  Hey, wanna try how magical <span className="text-indigo-500 font-bold">vocale ai</span> is? Join us now!
                </p>
              )}
            </div>
            <AuthForm>
              <Inputs id="email" placeholder="Enter Email" type="email" value={emailValue} onChange={onChange} />
              <Inputs
                id="password"
                placeholder={showLoginForm ? "Password" : "Create Password"}
                type="password"
                value={password}
                onChange={onPasswordChange}
              />
              {!showLoginForm && (
                <Inputs
                  id="confirmPassword"
                  placeholder="Confirm Password"
                  type="password"
                  value={confirmPassword}
                  onChange={onConfirmPasswordChange}
                />
              )}
              <Button label={showLoginForm ? "Sign in" : "Register"} type="submit" onClick={onSubmit} className="mt-4" />
            </AuthForm>
          </div>

          <div className="text-white text-sm mt-4">
            {showLoginForm ? "Don't have an account?" : "Already have an account?"}
            <button onClick={toggleForms} className="text-indigo-500 ml-1 focus:outline-none">
              {showLoginForm ? "Register now" : "Sign in"}
            </button>
          </div>

        </div>
      </div>
    </div>
  );
}
