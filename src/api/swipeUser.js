import axios from "axios";
import BASE_URL from "../constants/BASE_URL";

export default async function swipeUser(tg_id){
    let res = await axios.post(`${BASE_URL}/user/swipe`,{'tg_id':tg_id})
    return res
}