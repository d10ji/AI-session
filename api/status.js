export default function handler(req, res) {
  const maxDay = parseInt(process.env.MAX_DAY) || 1;
  res.setHeader('Cache-Control', 'no-store, no-cache');
  res.json({ maxDay });
}
