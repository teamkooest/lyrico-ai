import InputProps from "../../interfaces/InputInterface"

export default function Inputs({ type, id, placeholder }: InputProps) {
  return (
    <div className="w-full flex flex-col gap-2 items-start">
      <input type={type} id={id} className="shadow-sm bg-gray-700 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 outline-none block w-full p-2.5 px-4" placeholder={placeholder} required />
    </div>
  )
}
