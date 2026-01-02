import './App.css'

type MessageProps = {
  message: string
}

function Message({ message }: MessageProps) {
  return <div>{message}</div>
}

function App() {
  const message = "hello!"
  return (
    <>
      <Message message={message}/>
    </>
  )
}

export default App
