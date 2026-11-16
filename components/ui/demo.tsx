"use client"

import * as React from "react"
import StickerSlapFooter from "@/components/ui/sticker-slap-footer"

export default function Demo() {
  return (
    <div className="w-full">
      {/* University Yatra Neo-Brutalist Themed Sticker Slap Footer */}
      <StickerSlapFooter
        wordmark="yatra"
        homeHref="#top"
        navLabel="yatra"
        navHref="#top"
        chatLabel="chat with counsellor"
        chatHref="https://wa.me/919217368750"
        jobsLabel="study pathways"
        jobs={[
          { title: "direct study abroad", href: "#pathways" },
          { title: "fast track pathway (save 45%)", href: "#pathways" },
          { title: "study abroad cost calculator", href: "#calculator" },
        ]}
        officeLabel="destinations"
        address={[
          "germany (zero tuition)",
          "canada (3-year pgwp)",
          "united kingdom (1-year masters)",
          "australia & united states",
        ]}
        mapLabel="explore all countries"
        mapHref="#destinations"
        contactLabel="study support"
        email="info@universityyatra.com"
        copiedLabel="email copied!"
        note="*free 1-on-1 profile evaluation with senior counsellors."
        socials={[
          { kind: "instagram", href: "https://instagram.com" },
          { kind: "linkedin", href: "https://linkedin.com" },
          { kind: "youtube", href: "https://youtube.com" },
        ]}
        credits={[
          { role: "brand", name: "University Yatra" },
          { role: "entity", name: "Future Yatra Private Limited" },
          { role: "office", name: "Supernova Astralis, Sector 94, Noida" },
        ]}
        // University Yatra Neo-Brutalism Color Theme
        paper="#FFFDF5"
        panel="#1856F3"
        ink="#0A1230"
        cream="#FFFFFF"
        accent="#C8FF3E"
        fontSans="'Plus Jakarta Sans', system-ui, sans-serif"
        height="90svh"
      />
    </div>
  )
}

