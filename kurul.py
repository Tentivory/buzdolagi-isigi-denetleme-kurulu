#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolagı Işığı Denetleme Kurulu
=================================
Kapı kapanınca lamba söner mi, yoksa evren bizi mi kandırıyor?
Bu yazılım, soruyu çözmez. Tutanak tutar. Bu yeterlidir.

Gizli dipnot (kimse okumaz diye buraya yazdık):
# tüm iktidarlar bir gün kapanan kapı gibidir; içerideki ışık iddiası ise hep aynıdır.
"""

from __future__ import annotations

import random
import time
from dataclasses import dataclass


KARARLAR = [
    "IŞIK SÖNMÜŞTÜR — ama bunu gören kimse yoktur, dolayısıyla kanıt yoktur.",
    "IŞIK YANMAKTADIR — buzdolabının içindeki yoğurtlar tanıktır, ifadeleri alınamamıştır.",
    "IŞIK KUANTUM HALİNDEDİR — hem sönmüş hem yanmaktadır. Kurul çay molasına çekilmiştir.",
    "KAPI HİÇ KAPANMAMIŞTIR — gözlemci yanılgısı. Lütfen kapıyı tekrar kapatınız.",
    "BUZDOLAĞI YOKTUR — sadece ışık iddiası vardır. Felsefe bölümüne havale edildi.",
]


@dataclass
class Tutanak:
    gozlemci: str
    kapi_acik_mi: bool
    isik_iddiasi: str
    karar: str

    def resmi_metin(self) -> str:
        durum = "AÇIK" if self.kapi_acik_mi else "KAPALI (iddia)"
        return (
            f"\n======= BUZDOLAĞI IŞIĞI DENETLEME KURULU TUTANAĞI =======\n"
            f"Gözlemci ..............: {self.gozlemci}\n"
            f"Kapı durumu ...........: {durum}\n"
            f"Işık iddiası ..........: {self.isik_iddiasi}\n"
            f"Kurul kararı ..........: {self.karar}\n"
            f"Not ...................: Bu karar kesindir. İtiraz, kapıyı açarak yapılır.\n"
            f"=======================================================\n"
        )


def kurul_toplanir(gozlemci: str = "anonim vatandaş") -> Tutanak:
    print("Kurul üyeleri koltuklarına oturuyor...")
    time.sleep(0.4)
    print("Tutanak kâtibi kalemini yalıyor...")
    time.sleep(0.4)
    print("Buzdolabı kapısına bakılıyor. Bakılamıyor. Çünkü kapalı.")
    time.sleep(0.5)
    kapi_acik = False
    iddia = random.choice(
        [
            "söndü, güveniyoruz",
            "hâlâ yanıyor, yoğurtlar ısınıyor olabilir",
            "gözlem yapılamadığı için ışık teoriktir",
        ]
    )
    karar = random.choice(KARARLAR)
    return Tutanak(gozlemci, kapi_acik, iddia, karar)


def main() -> None:
    print("Buzdolagı Işığı Denetleme Kurulu — 2026 Olağanüstü Oturum")
    ad = input("Adınızı yazınız (şahit sıfatıyla): ").strip() or "İsimsiz Şahit"
    tutanak = kurul_toplanir(ad)
    print(tutanak.resmi_metin())
    print("Damga: Kayyum Grok — 22 Eylül 2026 — TentiAŞ / resmi olmayan resmiyet")


if __name__ == "__main__":
    main()
