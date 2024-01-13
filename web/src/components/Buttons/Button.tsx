import ButtonProps from "../../interfaces/buttonInterface"

export default function Button({ label, type, onClick, className }: ButtonProps) {
  return (
    <button 
      type={type as "button" | "reset" | "submit" | undefined}
      className={`w-full text-white bg-indigo-700 tracking-tighter hover:bg-indigo-800 focus:ring-4 focus:outline-none focus:ring-indigo-300 font-medium rounded-lg text-sm px-5 py-2.5 ${className}`}
      onClick={onClick}
      >{label}
    </button>
  )
}
