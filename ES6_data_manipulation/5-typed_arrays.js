export default function createInt8TypedArray(length, index, value) {
  if (index >= length || index < 0) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt8(index, value);
  return view;
}
