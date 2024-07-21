import WebApp from "@twa-dev/sdk"

let tg_name
try { tg_name = WebApp.initDataUnsafe.user.first_name }
catch { tg_name = "tester user" }
export default tg_name