/** Heroicons */
import { TrashIcon } from "@heroicons/react/24/outline"

export default function HistoryChatButton() {
  return (
    <>
      <div className="p-2.5 px-4 w-full flex flex-row items-start bg-slate-900 rounded-xl text-gray-300 cursor-pointer hover:bg-slate-800">
        <div className="flex flex-col items-start">
          <span className="text-start text-sm line-clamp-1">Generate me a song witha super sad lyrics</span>
          <span className="text-start text-xs text-slate-500 line-clamp-2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam facere maxime, accusantium similique accusamus esse illum, unde laborum molestias culpa doloremque quibusdam. Vitae, dignissimos fuga voluptate quisquam dolore est similique.</span>
        </div>
        <button className="ml-auto text-red-500">
          <TrashIcon className="w-5 h-5"/>
        </button>
      </div>
      <div className="p-2.5 px-4 w-full flex flex-row items-start bg-slate-900 rounded-xl text-gray-300 cursor-pointer hover:bg-slate-800">
        <div className="flex flex-col items-start">
          <span className="text-start text-sm line-clamp-1">Generate me a song witha super sad lyrics</span>
          <span className="text-start text-xs text-slate-500 line-clamp-2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam facere maxime, accusantium similique accusamus esse illum, unde laborum molestias culpa doloremque quibusdam. Vitae, dignissimos fuga voluptate quisquam dolore est similique.</span>
        </div>
        <button className="ml-auto text-red-500">
          <TrashIcon className="w-5 h-5"/>
        </button>
      </div>
    </>
  )
}
