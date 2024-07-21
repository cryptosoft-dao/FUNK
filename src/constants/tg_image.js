import WebApp from "@twa-dev/sdk"
import BASE_URL from "./BASE_URL"

let tg_image
console.log(WebApp.initDataUnsafe);
try { tg_image = WebApp.initDataUnsafe.user.photo_url }
catch { tg_image = BASE_URL + "/test_data/image" }
export default tg_image