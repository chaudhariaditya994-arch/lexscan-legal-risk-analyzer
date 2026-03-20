export function toBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => {
      const result = String(reader.result || "");
      resolve(result.split(",").pop() || "");
    };
    reader.onerror = () => reject(new Error("Unable to convert file to base64."));
    reader.readAsDataURL(file);
  });
}
