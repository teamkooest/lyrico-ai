/** Heroicons */
import { PlusIcon } from "@heroicons/react/24/solid"

export default function NewChatButton() {
  return (
    <button className="p-2.5 px-4 w-full flex flex-row items-center gap-2 justify-between bg-indigo-600 rounded-xl text-white tracking-tighter hover:bg-indigo-500">
      <span>New chat</span>
      <PlusIcon className="w-5 h-5"/>
    </button>
  )
}
