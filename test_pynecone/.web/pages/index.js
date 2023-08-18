import {useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Center, Circle, Divider, HStack, Heading, Select, Switch, VStack, option} from "@chakra-ui/react"
import NextHead from "next/head"

const EVENT = "ws://localhost:8000/event"
export default function Component() {
const [state, setState] = useState({"hour": 7, "hour_rotation": "rotate(120deg)", "meridiem": "AM", "minute": 46, "minute_display": "46", "minute_rotation": "rotate(186.55200000000002deg", "second": 6, "second_display": "06", "second_rotation": "rotate(-53.928000000000004deg)", "start": false, "zone": "US/Pacific", "events": [{"name": "state.hydrate"}]})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT)
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Center sx={{"padding": "5em"}}><VStack sx={{"padding": "5em", "borderWidth": "medium", "borderColor": "#43464B", "borderRadius": "25px", "bg": "#ededed", "textAlign": "center"}}><Circle sx={{"borderWidth": "thick", "borderColor": "#43464B", "width": "25em", "height": "25em", "bg": "rgb(250,250,250)", "boxShadow": "dark-lg"}}><Circle sx={{"width": "1em", "height": "1em", "borderWidth": "thick", "borderColor": "#43464B", "zIndex": 1}}/>
<Divider sx={{"transform": state.minute_rotation, "width": "18em", "position": "absolute", "borderStyle": "solid", "borderWidth": "4px", "borderImage": "linear-gradient(to right, rgb(250,250,250) 50%, red 100%) 0 0 100% 0", "zIndex": 0}}/>
<Divider sx={{"transform": state.hour_rotation, "width": "20em", "position": "absolute", "borderStyle": "solid", "borderWidth": "4px", "borderImage": "linear-gradient(to right, rgb(250,250,250) 50%, black 100%) 0 0 100% 0", "zIndex": 0}}/>
<Divider sx={{"transform": state.second_rotation, "width": "16em", "position": "absolute", "borderStyle": "solid", "borderWidth": "4px", "borderImage": "linear-gradient(to right, rgb(250,250,250) 50%, blue 100%) 0 0 100% 0", "zIndex": 0}}/></Circle>
<HStack><HStack sx={{"borderWidth": "medium", "borderColor": "#43464B", "borderRadius": "2em", "paddingX": "2em", "bg": "white", "color": "#333"}}><Heading>{state.hour}</Heading>
<Heading>{`:`}</Heading>
<Heading>{state.minute_display}</Heading>
<Heading>{`:`}</Heading>
<Heading>{state.second_display}</Heading>
<Heading>{state.meridiem}</Heading></HStack>
<Switch isChecked={state.start}
onChange={(_e) => Event([E("state.flip_switch", {start:_e.target.checked})])}/></HStack>
<Select placeholder="Select a time zone."
onChange={(_e) => Event([E("state.set_zone", {value:_e.target.value})])}
sx={{"bg": "#white"}}><option value="Asia/Tokyo">{`Asia/Tokyo`}</option>
<option value="Australia/Sydney">{`Australia/Sydney`}</option>
<option value="Europe/London">{`Europe/London`}</option>
<option value="Europe/Paris">{`Europe/Paris`}</option>
<option value="Europe/Moscow">{`Europe/Moscow`}</option>
<option value="US/Pacific">{`US/Pacific`}</option>
<option value="US/Eastern">{`US/Eastern`}</option></Select></VStack>
<NextHead><title>{`Clock`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta property="og:image"
content="favicon.ico"/></NextHead></Center>
)
}