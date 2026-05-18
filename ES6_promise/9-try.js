export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const res = mathFunction();
    queue.push(res);
  } catch (err) {
    queue.push(err);
  } finally {
    queue.push('Guardrail was executed');
  }

  return queue;
}
