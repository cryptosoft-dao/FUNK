import axios from "axios";
import BASE_URL from "../constants/BASE_URL";

export default async function getAds(startId) {
    let res = await axios.post(`${BASE_URL}/ads/all`, { 'startId': startId })
    return res
}