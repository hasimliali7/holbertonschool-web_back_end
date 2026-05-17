export default function getBudgetForKing(budget) {
  return {
    [`income-${budget.income}`]: budget.income,
    [`gdp-${budget.gdp}`]: budget.gdp,
    [`capita-${budget.capita}`]: budget.capita,
  };
}
