export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,147,190',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, the budget of San Francisco was ${budget.income}, the GDP was ${budget.gdp} and the GDP per capita was ${budget.capita}.`;
}
