export default function convertCoins(money) {
    let money_str = money.toString()
    if (money >= 100) { money_str = `${Math.floor((money / 1000) * 100) / 100}K` }
    if (money >= 100_000) { money_str = `${Math.floor((money / 1_000_000) * 100) / 100}M` }
    if (money >= 100_000_000) { money_str = `${Math.floor((money / 1_000_000_000) * 100) / 100}B` }
    return money_str
}
