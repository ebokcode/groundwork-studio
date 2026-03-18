// Twilio webhook — fires when someone replies to the Twilio number.
// Sends an instant email notification to evan@teamground.work via Resend.

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    // Parse Twilio's form-encoded body
    const params = new URLSearchParams(event.body);
    const from    = params.get("From")  || "Unknown";
    const body    = params.get("Body")  || "(no message)";
    const to      = params.get("To")    || "";
    const numMedia = params.get("NumMedia") || "0";

    const RESEND_API_KEY = process.env.RESEND_API_KEY;

    const emailBody = `
<div style="font-family:sans-serif;max-width:600px;margin:0 auto;">
  <div style="background:#1e4d2b;padding:16px 24px;border-radius:8px 8px 0 0;">
    <h2 style="color:#fff;margin:0;font-size:18px;">📱 New SMS Reply — Groundwork Studio</h2>
  </div>
  <div style="background:#f9fafb;padding:24px;border:1px solid #e5e7eb;border-radius:0 0 8px 8px;">
    <p style="margin:0 0 12px;"><strong>From:</strong> ${from}</p>
    <p style="margin:0 0 12px;"><strong>To (Twilio):</strong> ${to}</p>
    <p style="margin:0 0 12px;"><strong>Message:</strong></p>
    <div style="background:#fff;border:1px solid #d1d5db;border-radius:6px;padding:16px;font-size:16px;">
      ${body}
    </div>
    ${numMedia !== "0" ? `<p style="margin:12px 0 0;color:#6b7280;font-size:13px;">📎 ${numMedia} media attachment(s)</p>` : ""}
    <hr style="margin:20px 0;border:none;border-top:1px solid #e5e7eb;">
    <p style="margin:0;font-size:12px;color:#9ca3af;">
      Reply via <a href="https://console.twilio.com/us1/monitor/logs/sms">Twilio console</a> or text back from your Google Voice number (480) 382-2145
    </p>
  </div>
</div>`;

    await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${RESEND_API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        from: "Groundwork Studio Alerts <onboarding@resend.dev>",
        to:   ["evan@teamground.work"],
        subject: `💬 SMS Reply from ${from}`,
        html: emailBody,
      }),
    });

    // Return valid TwiML so Twilio doesn't show an error
    return {
      statusCode: 200,
      headers: { "Content-Type": "text/xml" },
      body: `<?xml version="1.0" encoding="UTF-8"?><Response></Response>`,
    };
  } catch (err) {
    console.error("sms-notify error:", err);
    return {
      statusCode: 200,
      headers: { "Content-Type": "text/xml" },
      body: `<?xml version="1.0" encoding="UTF-8"?><Response></Response>`,
    };
  }
};
