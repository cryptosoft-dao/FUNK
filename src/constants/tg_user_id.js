import WebApp from "@twa-dev/sdk"

let tg_user_id
try{tg_user_id = WebApp.initDataUnsafe.user.id}
catch{tg_user_id = 1}
export default tg_user_id