class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0] # 最初の価格を これまでの最低価格 として初期化
        max_profit = 0 # 初期の最大利益は0（取引しない場合）

        for price in prices:
            min_buy = min(min_buy, price) # より安い購入価格があれば更新
            max_profit = max(max_profit, price - min_buy) # より高い利益があれば更新

        return max_profit