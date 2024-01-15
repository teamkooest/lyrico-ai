/** Heroicons */
import { PaperAirplaneIcon } from "@heroicons/react/24/solid"

/** Components */
import Logo from "./components/Logos/Logo"
import NewChatButton from "./components/Buttons/NewChatButton"
import HistoryChatCard from "./components/Cards/HistoryChatCard"
import HelloWorld from "./components/Overlays/HelloWorld"
import ChatCard from "./components/Cards/ChatCard"

function App() {
  return (
    <main className="w-full h-full">
      <div className="fixed">
        <Logo />
      </div>
      <div className="p-18 w-full h-full flex flex-col items-center justify-center">
        <div className="flex flex-row items-center gap-2 h-[800px]">
          <div className="h-full flex flex-col gap-4 items-center w-64">
            <NewChatButton />
            <div className="pb-2 flex flex-col gap-2 items-center w-full overflow-y-auto">
              <HistoryChatCard />
            </div>
          </div>
          <div className="p-4 h-full border border-dashed border-slate-800 rounded-xl w-full max-w-2xl ">
            <div className="flex flex-col h-full relative">
              <HelloWorld />
              <div className="z-50 pb-4 flex flex-col items-center gap-4 w-full overflow-y-auto">
                <ChatCard />
              </div>
              <div className="z-50 mt-auto flex flex-row items-center gap-4 w-full justify-center">
                <input className="p-2.5 px-4 w-full max-w-xs h-full bg-slate-900 rounded-xl placeholder:text-slate-500 outline-none hover:max-w-md focus:max-w-md duration-300 transition-all ease-in-out" placeholder="Create a song."/>
                <PaperAirplaneIcon className="w-6 h-6 hover:text-indigo-500 cursor-pointer"/>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  )
}

export default App
