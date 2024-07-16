import axios from "axios";
import BASE_URL from "../constants/BASE_URL";

export default async function getAds(){
    let res = await axios.get(`${BASE_URL}/ads/all`)
    return res
}