import axios from "axios";
import BASE_URL from "../constants/BASE_URL";

export default async function getRefs(tg_user_id) {
    let res = await axios.post(`${BASE_URL}/ref/all`, { 'tg_id': tg_user_id })
    return res
}