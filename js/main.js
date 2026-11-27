/**
 * University Yatra — Study Abroad Landing Page
 * Step-by-Step Calculator & Official Country Guide Controller
 * Features Prev/Continue navigation, country dropdown two-way sync, authentic costs & PDF downloads
 */

(function () {
  'use strict';

  const WA_NUMBER = '919217368750';
  const SHEET_URL = 'https://script.google.com/macros/s/AKfycbz_q_6yX6UbnnPUMIZxPl0BV_FuH7zU7VXgMB1fsg2UEAmyaBgo77ku0kVy68GIvUZ4/exec';
  const $ = id => document.getElementById(id);
  const wa = m => 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(m);

  function postLeadToSheet(payload) {
    if (!SHEET_URL) return Promise.resolve();
    return fetch(SHEET_URL, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(payload)
    }).catch(() => {});
  }

  /* 100% Verified Logic Sheet Data for all 8 countries */
  const DOCX_DATA = {
    'Canada': {
      flag: '🇨🇦',
      name: 'Canada',
      currency: 'CAD',
      fx: 'CAD 1 = Rs. 65',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹91.5 L',
          ftAvailable: true,
          ftTotal: '≈ ₹66.3 L',
          ftSavings: '≈ ₹25.2 L',
          directLabel: 'Direct (3 yr abroad)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (CAD 23,000/yr)', direct: 'CAD 69,000 (Rs. 44,85,000)', ft: 'India Rs. 5,00,000 + CAD 46,000 (Rs. 29,90,000)' },
            { label: 'Living (CAD 23,448/yr)', direct: 'CAD 70,344 (Rs. 45,72,360)', ft: 'CAD 46,896 (Rs. 30,48,240) (1 yr saved)' },
            { label: 'One-time (Permit + Bio + Flight)', direct: 'CAD 1,435 (Rs. 93,275)', ft: 'CAD 1,435 (Rs. 93,275)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹65.2 L',
          ftAvailable: true,
          ftTotal: '≈ ₹55.0 L',
          ftSavings: '≈ ₹10.0 L',
          directLabel: 'Direct (2 yr abroad)',
          ftLabel: 'Fast Track (1 India + 16 mo abroad)',
          rows: [
            { label: 'Tuition (CAD 26,000/yr)', direct: 'CAD 52,000 (Rs. 33,80,000)', ft: 'India Rs. 5,00,000 + abroad tuition' },
            { label: 'Living (CAD 23,448/yr)', direct: 'CAD 46,896 (Rs. 30,48,240)', ft: '~16 months abroad' },
            { label: 'One-time (Permit + Bio + Flight)', direct: 'CAD 1,435 (Rs. 93,275)', ft: 'CAD 1,435 (Rs. 93,275)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹70.4 L',
          ftAvailable: true,
          ftTotal: '≈ ₹58.0 L',
          ftSavings: '≈ ₹12.0 L',
          directLabel: 'Direct (2 yr abroad)',
          ftLabel: 'Fast Track (1 India + 16 mo abroad)',
          rows: [
            { label: 'Tuition (CAD 30,000/yr)', direct: 'CAD 60,000 (Rs. 39,00,000)', ft: 'India Rs. 5,00,000 + abroad tuition' },
            { label: 'Living (CAD 23,448/yr)', direct: 'CAD 46,896 (Rs. 30,48,240)', ft: '~16 months abroad' },
            { label: 'One-time (Permit + Bio + Flight)', direct: 'CAD 1,435 (Rs. 93,275)', ft: 'CAD 1,435 (Rs. 93,275)' }
          ]
        }
      },
      timeline: {
        directPrep: '~8-9 months (offer letter, GIC, PAL, visa ~8-12 weeks)',
        recommendedIntake: 'September 2027 (Main) | May 2027 (Select programs)',
        directWait: '~10 months before going abroad',
        ftStart: 'Starts almost immediately - online from India within weeks',
        ftMove: 'Move abroad in ~10-11 months after India phase (qualifies for 3-yr PGWP)'
      },
      extraNote: 'Insurance is included by most Canadian universities. GIC is refundable proof of funds, not an extra cost.',
      disclaimer: 'Costs, intakes, and rules change - always verify with the university and embassy. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'September 2027 (Main) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuidePdf: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    },
    'Germany': {
      flag: '🇩🇪',
      name: 'Germany',
      currency: 'EUR',
      fx: 'EUR 1 = Rs. 100',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹85.6 L',
          ftAvailable: true,
          ftTotal: '≈ ₹62.3 L',
          ftSavings: '≈ ₹23.3 L',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (EUR 15,000/yr)', direct: 'EUR 45,000 (Rs. 45,00,000)', ft: 'India Rs. 5,00,000 + EUR 30,000 (Rs. 30,00,000)' },
            { label: 'Living (Blocked Acct EUR 11,904/yr)', direct: 'EUR 35,712 (Rs. 35,71,200)', ft: 'EUR 23,808 (Rs. 23,80,800) (1 yr saved)' },
            { label: 'Public Insurance (EUR 1,440/yr)', direct: 'EUR 4,320 (Rs. 4,32,000)', ft: 'EUR 2,880 (Rs. 2,88,000)' },
            { label: 'One-time (D Visa + Flight)', direct: 'EUR 575 (Rs. 57,500)', ft: 'EUR 575 (Rs. 57,500)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹45.7 L',
          ftAvailable: true,
          ftTotal: '≈ ₹34.1 L',
          ftSavings: '≈ ₹11.6 L',
          directLabel: 'Direct (Full abroad)',
          ftLabel: 'Fast Track (India + ~1.4 yr abroad)',
          rows: [
            { label: 'Tuition (Credit-based total)', direct: 'EUR 27,300 (Rs. 27.6 L)', ft: 'India Rs. 5,00,000 + EUR 16,620 (Rs. 16.8 L)' },
            { label: 'Living (Blocked Account)', direct: 'EUR 17,856 (Rs. 18.0 L)', ft: 'EUR 11,904 (Rs. 12.0 L)' },
            { label: 'Discount Included', direct: 'Base fee', ft: '20% discount included in Fast Track' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹49.0 L',
          ftAvailable: true,
          ftTotal: '≈ ₹37.0 L',
          ftSavings: '≈ ₹12.0 L',
          directLabel: 'Direct (Full abroad)',
          ftLabel: 'Fast Track (India + ~1.4 yr abroad)',
          rows: [
            { label: 'Program Structure', direct: 'Full 2-yr abroad (credit-based)', ft: '~6-8 mo India + ~1.4 yr abroad' },
            { label: 'Discount Included', direct: 'Base fee', ft: '20% discount included in Fast Track' }
          ]
        }
      },
      timeline: {
        directPrep: '~8-9 months (admission, blocked account, insurance, visa ~4-12 weeks)',
        recommendedIntake: 'Winter Semester (Sep-Oct 2027) | January 2028 (Secondary)',
        directWait: '~8-9 months before going abroad',
        ftStart: 'Starts almost immediately - online from India within weeks',
        ftMove: 'Fly out after India phase; 18-month job-seeker visa after graduation'
      },
      extraNote: 'Master\'s & MBA figures are credit-based overall totals with a 20% discount included in Fast Track.',
      disclaimer: 'Costs, intakes, scholarships and rules change - always verify with the university and the German mission. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'Winter Semester (Sep–Oct 2027) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'United Kingdom': {
      flag: '🇬🇧',
      name: 'United Kingdom',
      currency: 'GBP',
      fx: 'GBP 1 = Rs. 110',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹1.32 Cr',
          ftAvailable: true,
          ftTotal: '≈ ₹93.4 L',
          ftSavings: '≈ ₹38.6 L',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (GBP 28,000/yr)', direct: 'GBP 84,000 (Rs. 92,40,000)', ft: 'India Rs. 5,00,000 + GBP 56,000 (Rs. 61,60,000)' },
            { label: 'Living (UKVI GBP 10,827/yr)', direct: 'GBP 32,481 (Rs. 35,72,910)', ft: 'GBP 21,654 (Rs. 23,81,940) (1 yr saved)' },
            { label: 'IHS Health Surcharge (GBP 776/yr)', direct: 'GBP 2,328 (Rs. 2,56,080)', ft: 'GBP 1,552 (Rs. 1,70,720)' },
            { label: 'One-time (Visa + Flight)', direct: 'GBP 1,158 (Rs. 1,27,380)', ft: 'GBP 1,158 (Rs. 1,27,380)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹69.5 L',
          ftAvailable: true,
          ftTotal: '≈ ₹41.0 L',
          ftSavings: '≈ ₹28.5 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition (GBP 20,000/yr)', direct: 'GBP 40,000 (Rs. 44,00,000)', ft: 'India Rs. 5,00,000 + GBP 20,000 (Rs. 22,00,000)' },
            { label: 'Living (UKVI GBP 10,827/yr)', direct: 'GBP 21,654 (Rs. 23,81,940)', ft: 'GBP 10,827 (Rs. 11,90,970) (1 yr saved)' },
            { label: 'IHS Health Surcharge (GBP 776/yr)', direct: 'GBP 1,552 (Rs. 1,70,720)', ft: 'GBP 776 (Rs. 85,360)' },
            { label: 'One-time (Visa + Flight)', direct: 'GBP 1,158 (Rs. 1,27,380)', ft: 'GBP 1,158 (Rs. 1,27,380)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹69.5 L',
          ftAvailable: true,
          ftTotal: '≈ ₹41.0 L',
          ftSavings: '≈ ₹28.5 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition (GBP 20,000/yr)', direct: 'GBP 40,000 (Rs. 44,00,000)', ft: 'India Rs. 5,00,000 + GBP 20,000 (Rs. 22,00,000)' },
            { label: 'Living (UKVI GBP 10,827/yr)', direct: 'GBP 21,654 (Rs. 23,81,940)', ft: 'GBP 10,827 (Rs. 11,90,970) (1 yr saved)' },
            { label: 'IHS Health Surcharge (GBP 776/yr)', direct: 'GBP 1,552 (Rs. 1,70,720)', ft: 'GBP 776 (Rs. 85,360)' },
            { label: 'One-time (Visa + Flight)', direct: 'GBP 1,158 (Rs. 1,27,380)', ft: 'GBP 1,158 (Rs. 1,27,380)' }
          ]
        }
      },
      timeline: {
        directPrep: '~8-9 months (CAS, maintenance funds, visa ~3 weeks)',
        recommendedIntake: 'September 2027 (Main) | January 2028 (Backup)',
        directWait: '~8-9 months before going abroad',
        ftStart: 'Starts almost immediately - online from India within weeks',
        ftMove: 'Fly out after ~12 months; qualifies for 18-month UK Graduate Route'
      },
      extraNote: 'IHS covers NHS access, so no separate health insurance is needed.',
      disclaimer: 'Costs, intakes, and rules change - always verify with the university and UKVI. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'September 2027 (Main) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    },
    'Australia': {
      flag: '🇦🇺',
      name: 'Australia',
      currency: 'AUD',
      fx: 'AUD 1 = Rs. 58',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹1.16 Cr',
          ftAvailable: true,
          ftTotal: '≈ ₹82.8 L',
          ftSavings: '≈ ₹32.9 L',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (AUD 35,000/yr)', direct: 'AUD 105,000 (Rs. 60,90,000)', ft: 'India Rs. 5,00,000 + AUD 70,000 (Rs. 40,60,000)' },
            { label: 'Living (AUD 29,710/yr)', direct: 'AUD 89,130 (Rs. 51,69,540)', ft: 'AUD 59,420 (Rs. 34,46,360) (1 yr saved)' },
            { label: 'OSHC Health Cover (AUD 650/yr)', direct: 'AUD 1,950 (Rs. 1,13,100)', ft: 'AUD 1,300 (Rs. 75,400)' },
            { label: 'One-time (Visa 500 + Flight)', direct: 'AUD 3,500 (Rs. 2,03,000)', ft: 'AUD 3,500 (Rs. 2,03,000)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹72.0 L',
          ftAvailable: false,
          ftTotal: 'Direct Only',
          ftSavings: 'Direct Only',
          directLabel: 'Direct (2 yr on campus)',
          ftLabel: 'Not Available',
          rows: [
            { label: 'Tuition (AUD 30,000/yr)', direct: 'AUD 60,000 (Rs. 34,80,000)', ft: '-' },
            { label: 'Living (AUD 29,710/yr)', direct: 'AUD 59,420 (Rs. 34,46,360)', ft: '-' },
            { label: 'OSHC Health Cover (AUD 650/yr)', direct: 'AUD 1,300 (Rs. 75,400)', ft: '-' },
            { label: 'One-time (Visa 500 + Flight)', direct: 'AUD 3,500 (Rs. 2,03,000)', ft: '-' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹77.8 L',
          ftAvailable: false,
          ftTotal: 'Direct Only',
          ftSavings: 'Direct Only',
          directLabel: 'Direct (2 yr on campus)',
          ftLabel: 'Not Available',
          rows: [
            { label: 'Tuition (AUD 35,000/yr)', direct: 'AUD 70,000 (Rs. 40,60,000)', ft: '-' },
            { label: 'Living (AUD 29,710/yr)', direct: 'AUD 59,420 (Rs. 34,46,360)', ft: '-' },
            { label: 'OSHC Health Cover (AUD 650/yr)', direct: 'AUD 1,300 (Rs. 75,400)', ft: '-' },
            { label: 'One-time (Visa 500 + Flight)', direct: 'AUD 3,500 (Rs. 2,03,000)', ft: '-' }
          ]
        }
      },
      timeline: {
        directPrep: '~6-8 months (CoE, OSHC, GS statement, Subclass 500 visa)',
        recommendedIntake: 'July 2027 (Main) | February 2028 (Secondary)',
        directWait: '~6-8 months before going abroad (2+ yrs Post-Study 485 visa)',
        ftStart: 'Bachelor\'s only: Starts within weeks online from India (1 yr)',
        ftMove: 'Then 2 years in Australia - saves both time and money'
      },
      extraNote: 'Fast Track is available for Bachelor\'s only in Australia. Master\'s and MBA are Direct-only.',
      disclaimer: 'Costs, intakes, scholarships and rules change - always verify with the university and the Department of Home Affairs. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'July 2027 (Main) · February 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/Australia_Country_Guide_University_Yatra_v1.pdf'
    },
    'USA': {
      flag: '🇺🇸',
      name: 'USA',
      currency: 'USD',
      fx: 'USD 1 = Rs. 92',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹1.56 Cr',
          ftAvailable: true,
          ftTotal: '≈ ₹1.23 Cr',
          ftSavings: '≈ ₹33.6 L',
          directLabel: 'Direct (4 yr)',
          ftLabel: 'Fast Track (1 India + 3 abroad)',
          rows: [
            { label: 'Tuition ($22,000/yr)', direct: '$88,000 (Rs. 80,96,000)', ft: 'India Rs. 5,00,000 + $66,000 (Rs. 60,72,000)' },
            { label: 'Living ($18,000/yr)', direct: '$72,000 (Rs. 66,24,000)', ft: '$54,000 (Rs. 49,68,000) (1 yr saved)' },
            { label: 'Insurance ($2,000/yr)', direct: '$8,000 (Rs. 7,36,000)', ft: '$6,000 (Rs. 5,52,000)' },
            { label: 'One-time (SEVIS + MRV + Flight*)', direct: '$1,785 (Rs. 1,64,220)', ft: '$1,785 (Rs. 1,64,220)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹82.6 L',
          ftAvailable: true,
          ftTotal: '≈ ₹47.1 L',
          ftSavings: '≈ ₹35.5 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition ($24,000/yr)', direct: '$48,000 (Rs. 44,16,000)', ft: 'India Rs. 5,00,000 + $24,000 (Rs. 22,08,000)' },
            { label: 'Living ($18,000/yr)', direct: '$36,000 (Rs. 33,12,000)', ft: '$18,000 (Rs. 16,56,000) (1 yr saved)' },
            { label: 'Insurance ($2,000/yr)', direct: '$4,000 (Rs. 3,68,000)', ft: '$2,000 (Rs. 1,84,000)' },
            { label: 'One-time (SEVIS + MRV + Flight*)', direct: '$1,785 (Rs. 1,64,220)', ft: '$1,785 (Rs. 1,64,220)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹86.3 L',
          ftAvailable: true,
          ftTotal: '≈ ₹49.0 L',
          ftSavings: '≈ ₹37.3 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition ($26,000/yr)', direct: '$52,000 (Rs. 47,84,000)', ft: 'India Rs. 5,00,000 + $26,000 (Rs. 23,92,000)' },
            { label: 'Living ($18,000/yr)', direct: '$36,000 (Rs. 33,12,000)', ft: '$18,000 (Rs. 16,56,000) (1 yr saved)' },
            { label: 'Insurance ($2,000/yr)', direct: '$4,000 (Rs. 3,68,000)', ft: '$2,000 (Rs. 1,84,000)' },
            { label: 'One-time (SEVIS + MRV + Flight*)', direct: '$1,785 (Rs. 1,64,220)', ft: '$1,785 (Rs. 1,64,220)' }
          ]
        }
      },
      timeline: {
        directPrep: '~9-10 months (I-20, SEVIS, DS-160, interview, visa)',
        recommendedIntake: 'Fall 2027 (Sep-Oct) | January 2028 (Backup)',
        directWait: '~9-10 months before going abroad',
        ftStart: 'Starts almost immediately - online from India within weeks',
        ftMove: 'Fly out after ~12 months for campus phase, then OPT at graduation'
      },
      extraNote: '*One-time cost includes SEVIS $350, MRV $185, Flight $1,000, and $250 Visa Integrity Fee (subject to collection).',
      disclaimer: 'Costs, intakes, and rules change - always verify with the university and embassy. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'Fall 2027 (Sep–Oct) · January 2028 (Backup)',
      guidePdf: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/USA_Country_Guide_University_Yatra_v1.pdf'
    },
    'France': {
      flag: '🇫🇷',
      name: 'France',
      currency: 'EUR',
      fx: 'EUR 1 = Rs. 100',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹73.1 L',
          ftAvailable: true,
          ftTotal: '≈ ₹54.0 L',
          ftSavings: '≈ ₹19.1 L',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (EUR 12,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: 'India Rs. 5,00,000 + EUR 24,000 (Rs. 24,00,000)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: 'EUR 24,000 (Rs. 24,00,000) (1 yr saved)' },
            { label: 'CVEC Fee (EUR 105/yr)', direct: 'EUR 315 (Rs. 31,500)', ft: 'EUR 210 (Rs. 21,000)' },
            { label: 'One-time (Visa + Campus France + Flight)', direct: 'EUR 750 (Rs. 75,000)', ft: 'EUR 750 (Rs. 75,000)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹55.0 L',
          ftAvailable: true,
          ftTotal: '≈ ₹32.9 L',
          ftSavings: '≈ ₹22.1 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition (EUR 15,000/yr)', direct: 'EUR 30,000 (Rs. 30,00,000)', ft: 'India Rs. 5,00,000 + EUR 15,000 (Rs. 15,00,000)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 24,000 (Rs. 24,00,000)', ft: 'EUR 12,000 (Rs. 12,00,000) (1 yr saved)' },
            { label: 'CVEC Fee (EUR 105/yr)', direct: 'EUR 210 (Rs. 21,000)', ft: 'EUR 105 (Rs. 10,500)' },
            { label: 'One-time (Visa + Campus France + Flight)', direct: 'EUR 750 (Rs. 75,000)', ft: 'EUR 750 (Rs. 75,000)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹61.0 L',
          ftAvailable: false,
          ftTotal: 'Direct Only',
          ftSavings: 'Direct Only',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Not Available',
          rows: [
            { label: 'Tuition (EUR 18,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: '-' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 24,000 (Rs. 24,00,000)', ft: '-' },
            { label: 'CVEC Fee (EUR 105/yr)', direct: 'EUR 210 (Rs. 21,000)', ft: '-' },
            { label: 'One-time (Visa + Campus France + Flight)', direct: 'EUR 750 (Rs. 75,000)', ft: '-' }
          ]
        }
      },
      timeline: {
        directPrep: '~8-9 months (Campus France 4-8 weeks, visa 2-6 weeks)',
        recommendedIntake: 'September 2027 (Main) | January 2028 (Backup)',
        directWait: '~8-9 months before going abroad',
        ftStart: 'Bachelor\'s & Master\'s: Starts within weeks online from India',
        ftMove: 'Fly out after ~12 months; APS 12-month job-search permit for Master\'s'
      },
      extraNote: 'Health insurance is free in France (French public health). MBA is Direct-only (Fast Track not offered).',
      disclaimer: 'Costs, intakes, scholarships and rules change - always verify with the university and Campus France / the French consulate. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'September 2027 (Main) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Finland': {
      flag: '🇫🇮',
      name: 'Finland',
      currency: 'EUR',
      fx: 'EUR 1 = Rs. 100',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹77.6 L',
          ftAvailable: true,
          ftTotal: '≈ ₹57.1 L',
          ftSavings: '≈ ₹20.5 L',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Fast Track (1 India + 2 abroad)',
          rows: [
            { label: 'Tuition (EUR 13,000/yr)', direct: 'EUR 39,000 (Rs. 39,00,000)', ft: 'India Rs. 5,00,000 + EUR 26,000 (Rs. 26,00,000)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: 'EUR 24,000 (Rs. 24,00,000) (1 yr saved)' },
            { label: 'Insurance (EUR 500/yr)', direct: 'EUR 1,500 (Rs. 1,50,000)', ft: 'EUR 1,000 (Rs. 1,00,000)' },
            { label: 'One-time (Migri + Flight)', direct: 'EUR 1,100 (Rs. 1,10,000)', ft: 'EUR 1,100 (Rs. 1,10,000)' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹49.1 L',
          ftAvailable: true,
          ftTotal: '≈ ₹29.6 L',
          ftSavings: '≈ ₹19.5 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition (EUR 11,500/yr)', direct: 'EUR 23,000 (Rs. 23,00,000)', ft: 'India Rs. 4,50,000 + EUR 11,500 (Rs. 11,50,000)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 24,000 (Rs. 24,00,000)', ft: 'EUR 12,000 (Rs. 12,00,000) (1 yr saved)' },
            { label: 'Insurance (EUR 500/yr)', direct: 'EUR 1,000 (Rs. 1,00,000)', ft: 'EUR 500 (Rs. 50,000)' },
            { label: 'One-time (Migri + Flight)', direct: 'EUR 1,100 (Rs. 1,10,000)', ft: 'EUR 1,100 (Rs. 1,10,000)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹53.1 L',
          ftAvailable: true,
          ftTotal: '≈ ₹31.6 L',
          ftSavings: '≈ ₹21.5 L',
          directLabel: 'Direct (2 yr)',
          ftLabel: 'Fast Track (1 India + 1 abroad)',
          rows: [
            { label: 'Tuition (EUR 13,500/yr)', direct: 'EUR 27,000 (Rs. 27,00,000)', ft: 'India Rs. 4,50,000 + EUR 13,500 (Rs. 13,50,000)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 24,000 (Rs. 24,00,000)', ft: 'EUR 12,000 (Rs. 12,00,000) (1 yr saved)' },
            { label: 'Insurance (EUR 500/yr)', direct: 'EUR 1,000 (Rs. 1,00,000)', ft: 'EUR 500 (Rs. 50,000)' },
            { label: 'One-time (Migri + Flight)', direct: 'EUR 1,100 (Rs. 1,10,000)', ft: 'EUR 1,100 (Rs. 1,10,000)' }
          ]
        }
      },
      timeline: {
        directPrep: '~8-9 months (admission, Migri permit ~1-3 months, proof of funds)',
        recommendedIntake: 'Autumn 2027 (Sep-Oct) | January 2028 (Backup)',
        directWait: '~8-9 months before going abroad',
        ftStart: 'Starts almost immediately - online from India within weeks',
        ftMove: 'Fly out after ~12 months; up to 2 years post-study job-search permit'
      },
      extraNote: 'Living cost uses actual Helsinki estimate (EUR 12,000/yr). Migri visa proof of funds is EUR 9,600/yr.',
      disclaimer: 'Costs, intakes, scholarships and rules change - always verify with the university and Migri. All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'Autumn 2027 (Sep–Oct) · January 2028 (Secondary)',
      guidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf',
      ftGuidePdf: 'assets/pdfs/Germany_Country_Guide_University_Yatra_v2.pdf'
    },
    'Ireland': {
      flag: '🇮🇪',
      name: 'Ireland',
      currency: 'EUR',
      fx: 'EUR 1 = Rs. 100',
      levels: {
        "Bachelor's": {
          directTotal: '≈ ₹75.0 L',
          ftAvailable: false,
          ftTotal: 'Direct Only',
          ftSavings: 'Direct Only',
          directLabel: 'Direct (3 yr)',
          ftLabel: 'Not Available',
          rows: [
            { label: 'Tuition (EUR 12,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: '-' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 36,000 (Rs. 36,00,000)', ft: '-' },
            { label: 'Insurance (EUR 500/yr)', direct: 'EUR 1,500 (Rs. 1,50,000)', ft: '-' },
            { label: 'IRP Registration (EUR 300/yr)', direct: 'EUR 900 (Rs. 90,000)', ft: '-' },
            { label: 'One-time (D Visa + Flight)', direct: 'EUR 560 (Rs. 56,000)', ft: '-' }
          ]
        },
        "Master's": {
          directTotal: '≈ ₹36.7 L',
          ftAvailable: true,
          ftTotal: '≈ ₹35.0 L',
          ftSavings: '≈ ₹1.7 L',
          directLabel: 'Direct (1 yr on campus)',
          ftLabel: 'Fast Track (6 mo India + 1 yr campus)',
          rows: [
            { label: 'Tuition (Fast Track prog.)', direct: 'EUR 23,314 (Rs. 23,31,400)', ft: 'India Rs. 4,50,000 + EUR 17,151 (Rs. 17,15,100, 26% off)' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 12,000 (Rs. 12,00,000)', ft: 'EUR 12,000 (Rs. 12,00,000) (same)' },
            { label: 'Insurance + IRP', direct: 'EUR 800 (Rs. 80,000)', ft: 'EUR 800 (Rs. 80,000)' },
            { label: 'One-time (D Visa + Flight)', direct: 'EUR 560 (Rs. 56,000)', ft: 'EUR 560 (Rs. 56,000)' }
          ]
        },
        "MBA": {
          directTotal: '≈ ₹28.4 L',
          ftAvailable: false,
          ftTotal: 'Direct Only',
          ftSavings: 'Direct Only',
          directLabel: 'Direct (1 yr)',
          ftLabel: 'Not Available',
          rows: [
            { label: 'Tuition (EUR 15,000/yr)', direct: 'EUR 15,000 (Rs. 15,00,000)', ft: '-' },
            { label: 'Living (EUR 12,000/yr)', direct: 'EUR 12,000 (Rs. 12,00,000)', ft: '-' },
            { label: 'Insurance + IRP', direct: 'EUR 800 (Rs. 80,000)', ft: '-' },
            { label: 'One-time (D Visa + Flight)', direct: 'EUR 560 (Rs. 56,000)', ft: '-' }
          ]
        }
      },
      timeline: {
        directPrep: '~7-8 months (admission, funds, insurance, visa)',
        recommendedIntake: 'September 2027 (Main) | 2-yr Stay-Back Scheme',
        directWait: '~7-8 months before going abroad',
        ftStart: 'Master\'s only: Starts within weeks online from India (6 mo)',
        ftMove: 'Early start + stronger visa case, then 1 yr on campus'
      },
      extraNote: 'Fast Track is available for Master\'s only in Ireland. Bachelor\'s and MBA are Direct-only.',
      disclaimer: 'Costs, intakes, scholarships and rules change - always verify with the university and Irish immigration (ISD). All figures are planning estimates; scholarship amounts depend on merit and the university.',
      intake: 'September 2027 (Main)',
      guidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf',
      ftGuidePdf: 'assets/pdfs/UK_Country_Guide_University_Yatra_v1.pdf'
    },
    'Other': {
      flag: '🌐',
      name: 'Other',
      currency: 'USD',
      fx: 'Flexible Global FX',
      levels: {
        "Bachelor's": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Custom Savings', rows: [] },
        "Master's": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Custom Savings', rows: [] },
        "MBA": { directTotal: 'Custom Estimate', ftAvailable: true, ftTotal: 'Custom Fast Track', ftSavings: 'Custom Savings', rows: [] }
      },
      intake: 'Flexible Intakes across Europe, Asia & Overseas',
      guidePdf: 'assets/pdfs/Canada_Country_Guide_University_Yatra_v4.pdf',
      ftGuidePdf: 'assets/pdfs/University-Yatra-Canada-Fast-Track-Guide.pdf'
    }
  };

  const INTAKE_TABLE = {
    'Germany': '<strong>Germany Intakes:</strong> Main: Winter (<span class="intake-date-range">September–October</span>) &bull; Additional: <span class="intake-date-range">January</span>',
    'Canada': '<strong>Canada Intakes:</strong> Main: Fall (<span class="intake-date-range">September–October</span>) &bull; Additional: <span class="intake-date-range">January</span>',
    'USA': '<strong>USA Intakes:</strong> Main: Fall (<span class="intake-date-range">September–October</span>) &bull; Additional: <span class="intake-date-range">January</span>',
    'United Kingdom': '<strong>UK Intakes:</strong> Main: <span class="intake-date-range">September–October</span> &bull; Additional: <span class="intake-date-range">January</span>',
    'France': '<strong>France Intakes:</strong> Main: <span class="intake-date-range">September–October</span> &bull; Additional: <span class="intake-date-range">January</span>',
    'Australia': '<strong>Australia Intakes:</strong> Main: <span class="intake-date-range">February/March</span>, <span class="intake-date-range">July</span>',
    'Finland': '<strong>Finland Intakes:</strong> Main: Autumn (<span class="intake-date-range">September–October</span>) &bull; Additional: <span class="intake-date-range">January</span>',
    'Ireland': '<strong>Ireland Intakes:</strong> Main: <span class="intake-date-range">September–October</span>',
    'Other': '<strong>Other Destinations:</strong> Multiple flexible intakes across Europe, Asia &amp; overseas'
  };

  const FLAG_SVGS = {
    'Canada': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 0H8V32H0Z" fill="#D80027"/><path d="M24 0H32V32H24Z" fill="#D80027"/><path d="M16 6L17.5 11L21 10L19 13.5L22 15.5L17.5 18L17 22H15L14.5 18L10 15.5L13 13.5L11 10L14.5 11L16 6Z" fill="#D80027"/></svg>',
    'Germany': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H32V11H0Z" fill="#0A1230"/><path d="M0 11H32V21H0Z" fill="#DE0000"/><path d="M0 21H32V32H0Z" fill="#FFCE00"/></svg>',
    'United Kingdom': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#012169"/><path d="M0 0L32 32M32 0L0 32" stroke="#fff" stroke-width="4"/><path d="M0 0L32 32M32 0L0 32" stroke="#C8102E" stroke-width="2.2"/><path d="M16 0V32M0 16H32" stroke="#fff" stroke-width="6"/><path d="M16 0V32M0 16H32" stroke="#C8102E" stroke-width="3.6"/></svg>',
    'Australia': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#00008B"/><path d="M0 0H16V16H0Z" fill="#012169"/><path d="M0 0L16 16M16 0L0 16" stroke="#fff" stroke-width="2"/><path d="M0 0L16 16M16 0L0 16" stroke="#C8102E" stroke-width="1.2"/><path d="M8 0V16M0 8H16" stroke="#fff" stroke-width="3"/><path d="M8 0V16M0 8H16" stroke="#C8102E" stroke-width="1.8"/><circle cx="24" cy="8" r="1.5" fill="#fff"/><circle cx="27" cy="14" r="1.5" fill="#fff"/><circle cx="22" cy="20" r="1.5" fill="#fff"/><circle cx="25" cy="25" r="1.5" fill="#fff"/><circle cx="8" cy="24" r="2.5" fill="#fff"/></svg>',
    'USA': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 3H32M0 8H32M0 13H32M0 18H32M0 23H32M0 28H32" stroke="#B22234" stroke-width="2.6"/><rect width="15" height="16" fill="#3C3B6E"/><circle cx="4" cy="4" r="1" fill="#fff"/><circle cx="11" cy="4" r="1" fill="#fff"/><circle cx="7.5" cy="8" r="1" fill="#fff"/><circle cx="4" cy="12" r="1" fill="#fff"/><circle cx="11" cy="12" r="1" fill="#fff"/></svg>',
    'France': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#002654"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#ED2939"/></svg>',
    'Finland': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><rect width="32" height="32" fill="#FFFDF5"/><path d="M0 13H32V19H0Z" fill="#003580"/><path d="M10 0H16V32H10Z" fill="#003580"/></svg>',
    'Ireland': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><path d="M0 0H11V32H0Z" fill="#169B62"/><path d="M11 0H21V32H11Z" fill="#FFFFFF"/><path d="M21 0H32V32H21Z" fill="#FF883E"/></svg>',
    'Other': '<svg class="flag-svg" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg"><circle cx="16" cy="16" r="15" fill="#1856F3" stroke="#0A1230" stroke-width="1.8"/><ellipse cx="16" cy="16" rx="7" ry="14.5" fill="none" stroke="#C8FF3E" stroke-width="1.6"/><line x1="1.5" y1="16" x2="30.5" y2="16" stroke="#C8FF3E" stroke-width="1.6"/><line x1="3.5" y1="10" x2="28.5" y2="10" stroke="#FFFDF5" stroke-width="1.4"/><line x1="3.5" y1="22" x2="28.5" y2="22" stroke="#FFFDF5" stroke-width="1.4"/></svg>'
  };

  /* Current Active State */
  const S = {
    pathway: 'fast-track',
    level: "Master's",
    country: 'Canada',
    timeline: 'fall-2027'
  };

  let currentStep = 1;

  function resetResultGate() {
    const costsTable = $('lockedCostsTable');
    if (costsTable) costsTable.classList.remove('unlocked');
    const quickForm = $('calcQuickLeadForm');
    if (quickForm) {
      quickForm.classList.remove('is-hidden');
      quickForm.style.setProperty('display', 'flex');
      quickForm.reset();
    }
    const quickSuccess = $('calcQuickSuccess');
    if (quickSuccess) {
      quickSuccess.classList.remove('is-active');
      quickSuccess.style.setProperty('display', 'none');
    }
    const btn = $('calcQuickSubmitBtn');
    if (btn) {
      btn.disabled = false;
      const cName = S.country || 'Canada';
      btn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${cName} Cost Guide</span>`;
    }
    try {
      sessionStorage.removeItem('uy_calc_unlocked');
    } catch (e) {}
  }

  function updateStepView() {
    // Show/hide panes
    for (let i = 1; i <= 4; i++) {
      const pane = $('wizStep' + i);
      if (pane) pane.style.display = (currentStep === i) ? 'block' : 'none';
    }
    const resultPane = $('wizStepResult');
    if (resultPane) resultPane.style.display = (currentStep === 5) ? 'block' : 'none';

    // Update Progress Bar & Indicator
    const progressFill = $('wizProgressFill');
    const stepIndicator = $('wizStepIndicator');
    const prevBtn = $('wizPrevBtn');
    const nextBtn = $('wizNextBtn');

    if (currentStep <= 4) {
      // Clear unlocked / downloaded state when going back to previous steps
      resetResultGate();

      if (progressFill) progressFill.style.width = (currentStep * 25) + '%';
      if (stepIndicator) stepIndicator.textContent = 'Step ' + currentStep + ' of 4';
      if (prevBtn) prevBtn.style.visibility = (currentStep === 1) ? 'hidden' : 'visible';
      if (nextBtn) {
        nextBtn.style.display = 'inline-flex';
        nextBtn.innerHTML = (currentStep === 4) ? 'Calculate Cost <i class="fa-solid fa-calculator"></i>' : 'Continue <i class="fa-solid fa-arrow-right"></i>';
      }

      // Update dynamic intake schedule banner for chosen country
      const intakeTextEl = $('countryIntakeText');
      if (intakeTextEl) {
        intakeTextEl.innerHTML = INTAKE_TABLE[S.country] || INTAKE_TABLE['Canada'];
      }
    } else {
      // Step 5: Result View
      if (progressFill) progressFill.style.width = '100%';
      if (stepIndicator) stepIndicator.textContent = '';
      if (prevBtn) {
        prevBtn.style.visibility = 'visible';
        prevBtn.innerHTML = '<i class="fa-solid fa-arrow-left"></i> Edit Choices';
      }
      if (nextBtn) {
        nextBtn.style.display = 'none'; // Replaced by in-card lead form
      }
      calculateResults();
    }

    // Calculator smooth scroll alignment on step transition
    const fsModal = $('calcFullscreenModal');
    if (fsModal && !fsModal.hidden) {
      fsModal.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      const cardEl = $('calcWizardCard');
      if (cardEl) {
        const rect = cardEl.getBoundingClientRect();
        if (rect.top < 50 || rect.top > 160) {
          cardEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    }
  }

  function calculateResults() {
    const isOther = (S.country === 'Other');
    const cData = DOCX_DATA[S.country] || DOCX_DATA['Canada'];
    const lvlData = cData.levels[S.level] || cData.levels["Master's"];

    // DOM Updates
    const flagEl = $('rCountryFlag');
    const titleText = $('rTitleText');
    const lockedDocName = $('lockedCountryDocName');
    const otherBlock = $('otherCountryBlock');
    const lockedCard = document.querySelector('.locked-report-card');
    const quickForm = $('calcQuickLeadForm');
    const quickSuccess = $('calcQuickSuccess');
    const discEl = document.querySelector('.wiz-result-box .disc');

    if (otherBlock) otherBlock.style.display = isOther ? 'block' : 'none';
    if (lockedCard) lockedCard.style.display = isOther ? 'none' : 'block';

    // In 'Others', hide lead form and 'Download Free Global Study Guide' button completely as requested
    if (quickForm) {
      if (isOther) {
        quickForm.classList.add('is-hidden');
        quickForm.style.setProperty('display', 'none', 'important');
      } else {
        quickForm.classList.remove('is-hidden');
        quickForm.style.setProperty('display', 'flex');
      }
    }
    if (quickSuccess && isOther) {
      quickSuccess.classList.remove('is-active');
      quickSuccess.style.setProperty('display', 'none', 'important');
    }
    if (discEl) {
      discEl.style.display = isOther ? 'none' : 'flex';
    }
    const scholarshipNoteEl = $('calcScholarshipNote');
    if (scholarshipNoteEl) {
      scholarshipNoteEl.textContent = 'Up to 30% scholarship';
    }

    if (flagEl) flagEl.innerHTML = FLAG_SVGS[S.country] || FLAG_SVGS['Canada'];
    if (titleText) titleText.textContent = isOther ? `Other Destinations · ${S.level} Programme` : `${S.country} · ${S.level} Programme`;
    if (lockedDocName) lockedDocName.textContent = `${S.country} Complete Cost Guide`;

    // Exact Verified Figures (Blurred Behind Padlock until Lead submit)
    const blurDirect = $('blurDirectTotal');
    const blurFt = $('blurFtTotal');
    const blurSav = $('blurSavings');

    if (blurDirect) blurDirect.textContent = lvlData.directTotal;
    if (blurFt) blurFt.textContent = lvlData.ftTotal;
    if (blurSav) blurSav.textContent = lvlData.ftSavings;

    if (!isOther) {
      // Check if user already unlocked this destination in current session
      try {
        const unlockedCountry = sessionStorage.getItem('uy_calc_unlocked');
        if (unlockedCountry && unlockedCountry === S.country) {
          const costsTable = $('lockedCostsTable');
          if (costsTable) costsTable.classList.add('unlocked');
          if (quickForm) {
            quickForm.classList.add('is-hidden');
            quickForm.style.setProperty('display', 'none', 'important');
          }
          if (quickSuccess) {
            quickSuccess.classList.add('is-active');
            quickSuccess.style.setProperty('display', 'block', 'important');
            const scName = $('successCountryName');
            if (scName) scName.textContent = S.country;
          }
        }
      } catch (e) {}
    }
  }

  function pdfSafe(str) {
    return String(str || '')
      .replace(/₹/g, 'Rs. ')
      .replace(/≈/g, '~')
      .replace(/[–—]/g, '-')
      .replace(/·/g, '|')
      .replace(/[^\x20-\x7E]/g, '');
  }

  function wrapLines(text, maxChars) {
    const words = pdfSafe(text).split(/\s+/);
    const lines = [];
    let cur = '';
    for (const w of words) {
      if (!cur) { cur = w; }
      else if ((cur + ' ' + w).length <= maxChars) { cur += ' ' + w; }
      else { lines.push(cur); cur = w; }
    }
    if (cur) lines.push(cur);
    return lines;
  }

  function formatTimelineLabel(val) {
    if (val === 'immediate') return 'Immediate Start';
    if (val === 'fall-2027') return 'Fall 2027 (Sep-Oct)';
    if (val === 'jan-2028' || val === 'spring-2028') return 'January 2028';
    return val || 'Fall 2027 (Sep-Oct)';
  }

  let lastLeadInfo = { name: 'Student' };

  async function downloadPersonalizedPdf(country, state, lead) {
    const cData = DOCX_DATA[country] || DOCX_DATA['Canada'];
    const isFT = state.pathway === 'fast-track';
    const guidePdf = isFT ? cData.ftGuidePdf : cData.guidePdf;
    const filename = `University-Yatra-${country.replace(/\s+/g, '-')}-Cost-Guide.pdf`;

    if (!window.PDFLib || country === 'Other') {
      const a = document.createElement('a');
      a.href = guidePdf;
      a.setAttribute('download', filename);
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      return;
    }

    try {
      const { PDFDocument, rgb, StandardFonts } = window.PDFLib;
      const existingBytes = await fetch(guidePdf).then(r => {
        if (!r.ok) throw new Error('PDF fetch failed');
        return r.arrayBuffer();
      });
      const pdfDoc = await PDFDocument.load(existingBytes);
      const page = pdfDoc.insertPage(0, [595.28, 841.89]);
      const W = 595.28;
      const H = 841.89;

      const fontReg = await pdfDoc.embedFont(StandardFonts.Helvetica);
      const fontBold = await pdfDoc.embedFont(StandardFonts.HelveticaBold);

      // Theme colors matching University Yatra Country Guide PDFs
      const C_WHITE = rgb(1, 1, 1);
      const C_DARK = rgb(0.06, 0.09, 0.16);
      const C_BLUE = rgb(0.094, 0.337, 0.953); // #1856F3
      const C_MUTED = rgb(0.28, 0.33, 0.41);
      const C_CARD_BG = rgb(0.945, 0.965, 1.0); // #F1F6FF
      const C_BORDER = rgb(0.84, 0.89, 0.98);
      const C_ROW_ALT = rgb(0.975, 0.985, 1.0);

      // Background
      page.drawRectangle({ x: 0, y: 0, width: W, height: H, color: C_WHITE });

      // Top Header: Logo + Outlined Pill Badge
      let logoDrawn = false;
      try {
        const logoRes = await fetch('assets/logo.png');
        if (logoRes.ok) {
          const logoBytes = await logoRes.arrayBuffer();
          const logoImg = await pdfDoc.embedPng(logoBytes);
          const dims = logoImg.scaleToFit(120, 32);
          page.drawImage(logoImg, { x: 42, y: H - 58, width: dims.width, height: dims.height });
          logoDrawn = true;
        }
      } catch (e) {}
      if (!logoDrawn) {
        page.drawText('university yatra', { x: 42, y: H - 48, size: 15, font: fontBold, color: C_BLUE });
      }

      // Top-right badge
      page.drawRectangle({
        x: 382, y: H - 54, width: 171, height: 22,
        borderColor: C_BLUE, borderWidth: 1, color: C_WHITE
      });
      page.drawText('PERSONALIZED COST & TIMELINE', {
        x: 392, y: H - 47, size: 8, font: fontBold, color: C_BLUE
      });

      // Hero Title
      page.drawText('Your Study Plan for', { x: 42, y: H - 102, size: 28, font: fontBold, color: C_DARK });
      page.drawText(pdfSafe(country + '.'), { x: 42, y: H - 134, size: 28, font: fontBold, color: C_BLUE });

      const studentName = pdfSafe((lead && lead.name) ? lead.name.trim() : 'Student');
      const routeLabel = isFT ? 'Fast Track Pathway' : 'Regular Admission';
      const timelineLabel = formatTimelineLabel(state.timeline);
      const subText = `Prepared for ${studentName}  |  ${state.level}  |  ${routeLabel}  |  ${timelineLabel}`;
      page.drawText(pdfSafe(subText), { x: 42, y: H - 156, size: 9.5, font: fontReg, color: C_MUTED });

      // Selections Summary Strip (4 boxes)
      const selY = H - 210;
      const boxW = 123;
      const selItems = [
        { k: 'COUNTRY', v: country },
        { k: 'DEGREE LEVEL', v: state.level },
        { k: 'SELECTED ROUTE', v: routeLabel },
        { k: 'TARGET TIMELINE', v: timelineLabel }
      ];
      selItems.forEach((item, idx) => {
        const bx = 42 + idx * (boxW + 7);
        page.drawRectangle({ x: bx, y: selY, width: boxW, height: 40, color: C_CARD_BG, borderColor: C_BORDER, borderWidth: 0.8 });
        page.drawText(pdfSafe(item.k), { x: bx + 8, y: selY + 26, size: 6.5, font: fontBold, color: C_BLUE });
        page.drawText(pdfSafe(item.v), { x: bx + 8, y: selY + 11, size: 8.5, font: fontBold, color: C_DARK });
      });

      // Cost Breakdown Section
      const lvlData = cData.levels[state.level] || cData.levels["Master's"];
      const fxLine = `Cost Breakdown (${cData.fx}) - Base planning estimates before scholarship`;
      let curY = selY - 24;
      page.drawText(pdfSafe(fxLine), { x: 42, y: curY, size: 12, font: fontBold, color: C_DARK });
      curY -= 16;

      const tableLeft = 42;
      const tableW = 511;
      const hasFT = !!lvlData.ftAvailable;
      const col1W = hasFT ? 175 : 230;
      const col2W = hasFT ? 162 : 281;
      const col3W = hasFT ? 174 : 0;

      // Table Header
      page.drawRectangle({ x: tableLeft, y: curY - 22, width: col1W + col2W, height: 22, color: C_CARD_BG, borderColor: C_BORDER, borderWidth: 0.8 });
      page.drawText('Component', { x: tableLeft + 8, y: curY - 14, size: 8.5, font: fontBold, color: C_DARK });
      page.drawText(pdfSafe(lvlData.directLabel || 'Direct Route'), { x: tableLeft + col1W + 8, y: curY - 14, size: 8.5, font: fontBold, color: C_DARK });
      if (hasFT) {
        page.drawRectangle({ x: tableLeft + col1W + col2W, y: curY - 22, width: col3W, height: 22, color: C_BLUE });
        page.drawText(pdfSafe(lvlData.ftLabel || 'Fast Track (Recommended)'), { x: tableLeft + col1W + col2W + 8, y: curY - 14, size: 8.2, font: fontBold, color: C_WHITE });
      }
      curY -= 22;

      // Table Rows
      const rows = lvlData.rows || [];
      rows.forEach((row, rIdx) => {
        const dLines = wrapLines(row.direct, hasFT ? 30 : 48);
        const fLines = hasFT ? wrapLines(row.ft, 32) : [];
        const lLines = wrapLines(row.label, hasFT ? 30 : 40);
        const maxLines = Math.max(dLines.length, fLines.length, lLines.length, 1);
        const rowH = Math.max(22, maxLines * 11 + 10);

        const bg = rIdx % 2 === 1 ? C_ROW_ALT : C_WHITE;
        page.drawRectangle({ x: tableLeft, y: curY - rowH, width: tableW, height: rowH, color: bg, borderColor: C_BORDER, borderWidth: 0.6 });
        if (hasFT) {
          page.drawRectangle({ x: tableLeft + col1W + col2W, y: curY - rowH, width: col3W, height: rowH, color: rgb(0.93, 0.96, 1.0), borderColor: C_BORDER, borderWidth: 0.6 });
        }

        lLines.forEach((ln, i) => page.drawText(ln, { x: tableLeft + 8, y: curY - 13 - i * 11, size: 8, font: fontBold, color: C_DARK }));
        dLines.forEach((ln, i) => page.drawText(ln, { x: tableLeft + col1W + 8, y: curY - 13 - i * 11, size: 8, font: fontReg, color: C_MUTED }));
        if (hasFT) {
          fLines.forEach((ln, i) => page.drawText(ln, { x: tableLeft + col1W + col2W + 8, y: curY - 13 - i * 11, size: 8, font: fontReg, color: C_DARK }));
        }
        curY -= rowH;
      });

      // Total Row
      const totalH = 26;
      page.drawRectangle({ x: tableLeft, y: curY - totalH, width: col1W + col2W, height: totalH, color: C_CARD_BG, borderColor: C_BORDER, borderWidth: 0.8 });
      page.drawText('Estimated Total', { x: tableLeft + 8, y: curY - 17, size: 9, font: fontBold, color: C_DARK });
      page.drawText(pdfSafe(lvlData.directTotal), { x: tableLeft + col1W + 8, y: curY - 17, size: 9.5, font: fontBold, color: C_DARK });
      if (hasFT) {
        page.drawRectangle({ x: tableLeft + col1W + col2W, y: curY - totalH, width: col3W, height: totalH, color: C_BLUE });
        page.drawText(pdfSafe(lvlData.ftTotal), { x: tableLeft + col1W + col2W + 8, y: curY - 17, size: 9.5, font: fontBold, color: C_WHITE });
      }
      curY -= totalH;

      // Savings Highlight Bar (when Fast Track is available)
      if (hasFT) {
        curY -= 8;
        page.drawRectangle({ x: tableLeft, y: curY - 28, width: tableW, height: 28, color: C_BLUE });
        page.drawText(pdfSafe(`You save ${lvlData.ftSavings} with University Yatra Fast Track`), {
          x: tableLeft + 12, y: curY - 18, size: 10.5, font: fontBold, color: C_WHITE
        });
        curY -= 32;
      } else {
        curY -= 12;
        page.drawRectangle({ x: tableLeft, y: curY - 24, width: tableW, height: 24, color: C_CARD_BG, borderColor: C_BORDER, borderWidth: 0.8 });
        page.drawText(pdfSafe(`Note: Fast Track is not offered for ${state.level} in ${country}. Direct admission applies.`), {
          x: tableLeft + 10, y: curY - 15, size: 8.5, font: fontBold, color: C_BLUE
        });
        curY -= 28;
      }

      // Scholarship & Extra Note
      curY -= 6;
      const scholLines = wrapLines('Up to 30% additional scholarship / discount may be available depending on merit and the university. Figures above are base estimates.', 92);
      const extraLines = cData.extraNote ? wrapLines(cData.extraNote, 92) : [];
      const noteBoxH = (scholLines.length + extraLines.length) * 11 + 14;
      page.drawRectangle({ x: tableLeft, y: curY - noteBoxH, width: tableW, height: noteBoxH, color: C_ROW_ALT, borderColor: C_BORDER, borderWidth: 0.7 });
      let ny = curY - 13;
      scholLines.forEach(ln => { page.drawText(ln, { x: tableLeft + 10, y: ny, size: 8, font: fontBold, color: C_DARK }); ny -= 11; });
      extraLines.forEach(ln => { page.drawText(ln, { x: tableLeft + 10, y: ny, size: 7.5, font: fontReg, color: C_MUTED }); ny -= 11; });
      curY -= (noteBoxH + 16);

      // Timeline & Intake Recommendation
      page.drawText('Intake & Timeline Roadmap', { x: 42, y: curY, size: 12, font: fontBold, color: C_DARK });
      curY -= 12;

      const tl = cData.timeline || {};
      const tlCardW = hasFT ? 250 : tableW;
      const tlCardH = 86;

      // Direct Timeline Card
      page.drawRectangle({ x: tableLeft, y: curY - tlCardH, width: tlCardW, height: tlCardH, color: C_CARD_BG, borderColor: C_BORDER, borderWidth: 0.8 });
      page.drawText('Direct Route Timeline', { x: tableLeft + 10, y: curY - 16, size: 9, font: fontBold, color: C_DARK });
      let dy = curY - 30;
      wrapLines('Intake: ' + (tl.recommendedIntake || ''), hasFT ? 46 : 90).forEach(ln => {
        page.drawText(ln, { x: tableLeft + 10, y: dy, size: 7.8, font: fontReg, color: C_MUTED }); dy -= 11;
      });
      wrapLines('Prep: ' + (tl.directPrep || ''), hasFT ? 46 : 90).forEach(ln => {
        page.drawText(ln, { x: tableLeft + 10, y: dy, size: 7.8, font: fontReg, color: C_MUTED }); dy -= 11;
      });
      wrapLines('Wait: ' + (tl.directWait || ''), hasFT ? 46 : 90).forEach(ln => {
        page.drawText(ln, { x: tableLeft + 10, y: dy, size: 7.8, font: fontReg, color: C_MUTED }); dy -= 11;
      });

      // Fast Track Timeline Card
      if (hasFT) {
        const fxX = tableLeft + tlCardW + 11;
        page.drawRectangle({ x: fxX, y: curY - tlCardH, width: tlCardW, height: tlCardH, color: C_BLUE });
        page.drawText('Fast Track Timeline (Recommended)', { x: fxX + 10, y: curY - 16, size: 9, font: fontBold, color: C_WHITE });
        let fy = curY - 30;
        wrapLines(tl.ftStart || '', 46).forEach(ln => {
          page.drawText(ln, { x: fxX + 10, y: fy, size: 7.8, font: fontReg, color: C_WHITE }); fy -= 11;
        });
        wrapLines(tl.ftMove || '', 46).forEach(ln => {
          page.drawText(ln, { x: fxX + 10, y: fy, size: 7.8, font: fontReg, color: C_WHITE }); fy -= 11;
        });
        page.drawText('No long idle wait - study begins now.', { x: fxX + 10, y: fy - 2, size: 7.8, font: fontBold, color: C_WHITE });
      }

      // Footer Disclaimer
      const discLines = wrapLines(cData.disclaimer || 'All figures are planning estimates.', 102);
      let fyFoot = 48;
      discLines.forEach(ln => {
        page.drawText(ln, { x: 42, y: fyFoot, size: 7, font: fontReg, color: C_MUTED });
        fyFoot -= 9;
      });
      page.drawText('universityyatra.com  |  info@universityyatra.com  |  WhatsApp: +91 92173 68750', {
        x: 42, y: 20, size: 7.5, font: fontBold, color: C_BLUE
      });

      const pdfBytes = await pdfDoc.save();
      const blob = new Blob([pdfBytes], { type: 'application/pdf' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 5000);
    } catch (err) {
      const a = document.createElement('a');
      a.href = guidePdf;
      a.setAttribute('download', filename);
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    }
  }

  function initWizardController() {
    const card = $('calcWizardCard');
    if (!card) return;

    // Option item selection
    card.querySelectorAll('.wiz-opt').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const parentGrid = btn.parentElement;
        parentGrid.querySelectorAll('.wiz-opt').forEach(b => b.classList.remove('on'));
        btn.classList.add('on');

        const key = btn.dataset.k;
        const val = btn.dataset.v;
        if (key && val) {
          S[key] = val;
        }
      });
    });

    // Previous Button
    const prevBtn = $('wizPrevBtn');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        if (currentStep > 1) {
          currentStep--;
          updateStepView();
        }
      });
    }

    // Continue / Next Button
    const nextBtn = $('wizNextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (currentStep < 5) {
          currentStep++;
          updateStepView();
        }
      });
    }

    // In-Card Delivery Form
    const quickForm = $('calcQuickLeadForm');
    const quickSuccess = $('calcQuickSuccess');
    if (quickForm && quickSuccess) {
      quickForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const fd = new FormData(quickForm);
        const phone = String(fd.get('phone') || '').trim();
        const phoneCode = String(fd.get('phone_code') || '+91').trim();
        const name = String(fd.get('name') || '').trim();
        const email = String(fd.get('email') || '').trim();
        const country = S.country || 'Canada';
        const isOther = (country === 'Other');

        if (phone.length < 7 || phone.length > 12) {
          alert('Please enter a valid mobile number');
          return;
        }

        lastLeadInfo = { name, phone: `${phoneCode} ${phone}`, email };

        const cData = DOCX_DATA[country] || DOCX_DATA['Canada'];
        const lvlData = (cData && cData.levels && (cData.levels[S.level] || cData.levels["Master's"])) || {};
        postLeadToSheet({
          type: 'calculator',
          name,
          mobile: `${phoneCode} ${phone}`,
          qualification: email || S.level,
          country,
          pathway: S.pathway === 'fast-track' ? 'Fast Track' : 'Regular Admission',
          course: S.level,
          budget: formatTimelineLabel(S.timeline),
          tuition: lvlData.directTotal || '',
          living: lvlData.ftTotal || '',
          total: lvlData.ftSavings || '',
          page: window.location.href
        });

        const btn = $('calcQuickSubmitBtn');
        if (btn) {
          btn.disabled = true;
          btn.innerHTML = isOther ?
            `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing Global Study Guide...</span>` :
            `<i class="fa-solid fa-spinner fa-spin"></i> <span>Preparing ${country} Cost Guide...</span>`;
        }

        setTimeout(async () => {
          // Trigger personalized PDF generation & download (Page 1 generated + static guide from Page 2)
          await downloadPersonalizedPdf(country, { ...S }, lastLeadInfo);

          // Reset the submit button state so it is never permanently stuck on spinner
          if (btn) {
            btn.disabled = false;
            btn.innerHTML = isOther ?
              `<i class="fa-solid fa-lock-open"></i> <span>Download Free Global Study Guide</span>` :
              `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${country} Cost Guide</span>`;
          }

          // Unblur and reveal the personalized figures upon unlock!
          const costsTable = $('lockedCostsTable');
          if (costsTable) costsTable.classList.add('unlocked');

          // Cleanly hide lead form (both class and inline !important)
          quickForm.classList.add('is-hidden');
          quickForm.style.setProperty('display', 'none', 'important');

          // Update country name on success banner and cleanly show it
          const scName = $('successCountryName');
          if (scName) scName.textContent = isOther ? 'Global Study Abroad' : country;
          quickSuccess.classList.add('is-active');
          quickSuccess.style.setProperty('display', 'block', 'important');

          // Save unlocked state to sessionStorage
          try {
            sessionStorage.setItem('uy_calc_unlocked', country);
          } catch (e) {}
        }, 250);
      });
    }

    // Download Again button inside success view
    const downloadAgainBtn = $('calcDownloadAgainBtn');
    if (downloadAgainBtn) {
      downloadAgainBtn.addEventListener('click', () => {
        const country = S.country || 'Canada';
        downloadPersonalizedPdf(country, { ...S }, lastLeadInfo);
      });
    }

    // Reset button inside success view
    const resetBtn = $('calcResetBtn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        resetResultGate();
        currentStep = 1;
        updateStepView();
        const calcEl = $('calculator');
        if (calcEl) calcEl.scrollIntoView({ behavior: 'smooth' });
      });
    }

    // Prevent stuck disabled/loading buttons when returning from another tab or BFCache
    window.addEventListener('pageshow', () => {
      const btn = $('calcQuickSubmitBtn');
      if (btn && btn.disabled) {
        btn.disabled = false;
        const cName = S.country || 'Canada';
        btn.innerHTML = `<i class="fa-solid fa-lock-open"></i> <span>Download Free ${cName} Cost Guide</span>`;
      }
    });

    const startBtn = $('calcStartBtn');
    const fsModal = $('calcFullscreenModal');
    const fsBackBtn = $('calcFsBackBtn');

    function openCalcFullscreen() {
      if (!fsModal) return;
      fsModal.hidden = false;
      document.body.classList.add('calc-fs-open');
      fsModal.scrollTo({ top: 0, behavior: 'auto' });
    }

    function closeCalcFullscreen() {
      if (!fsModal) return;
      fsModal.hidden = true;
      document.body.classList.remove('calc-fs-open');
      const calcSec = $('calculator');
      if (calcSec) calcSec.scrollIntoView({ behavior: 'auto', block: 'start' });
    }

    if (startBtn) startBtn.addEventListener('click', openCalcFullscreen);
    if (fsBackBtn) fsBackBtn.addEventListener('click', closeCalcFullscreen);
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && fsModal && !fsModal.hidden) {
        closeCalcFullscreen();
      }
    });

    updateStepView();
  }

  // Country Quick Shortcut for Destination Cards
  window.startCountryGuide = function(cKey) {
    const map = {
      'germany': 'Germany',
      'canada': 'Canada',
      'uk': 'United Kingdom',
      'australia': 'Australia',
      'usa': 'USA',
      'france': 'France',
      'finland': 'Finland',
      'ireland': 'Ireland',
      'other': 'Other'
    };
    const cName = map[String(cKey).toLowerCase()] || 'Canada';
    const btn = document.querySelector(`.wiz-opt[data-k="country"][data-v="${cName}"]`);
    if (btn) btn.click();
    const calcEl = document.getElementById('calculator');
    if (calcEl) calcEl.scrollIntoView({ behavior: 'smooth' });
  };

  /* Bottom Enquiry Form (Name, Mobile, Email, Qualification, Destination, Course) */
  function initBottomEnquiry() {
    const form = $('enquiryForm');
    const ok = $('enquirySuccess');
    if (!form || !ok) return;

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const fd = new FormData(form);
      const name = String(fd.get('name') || '').trim();
      const phone = String(fd.get('mobile') || '').trim();
      const email = String(fd.get('email') || '').trim();
      const qual = String(fd.get('qualification') || '').trim();
      const country = String(fd.get('country') || '').trim();
      const course = String(fd.get('course') || '').trim();

      const countryCode = String(fd.get('country_code') || '+91').trim();

      if (countryCode === '+91') {
        if (!/^[6-9][0-9]{9}$/.test(phone)) {
          alert('Please enter a valid 10-digit Indian WhatsApp number');
          return;
        }
      } else {
        if (!/^[0-9]{7,15}$/.test(phone)) {
          alert('Please enter a valid phone number');
          return;
        }
      }

      const btn = $('enquirySubmitBtn');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting Enquiry...';
      }

      postLeadToSheet({
        type: 'enquiry',
        name,
        mobile: `${countryCode} ${phone}`,
        email,
        qualification: qual,
        destination: country,
        course,
        page: window.location.href
      });

      setTimeout(() => {
        form.style.display = 'none';
        ok.style.display = 'block';
        const sub = ok.querySelector('p');
        if (sub) {
          sub.innerHTML = `Your enquiry has been received. Our team will contact you at <strong>${countryCode} ${phone}</strong> shortly.`;
        }
      }, 500);
    });
  }

  /* ==========================================================================
     UNIVERSITY YATRA — STICKER SLAP FOOTER CONTROLLER
     Interactive Neo-Brutalist Studio Footer with Draggable Physics & SVG Marker
     ========================================================================== */
  function initStickerSlapFooter() {
    const footer = document.querySelector('.ssf');
    if (!footer) return;

    // 1. Stamp real path lengths for smooth SVG draw-in animation
    function stampLengths() {
      footer.querySelectorAll('path[data-draw]').forEach(p => {
        try {
          const l = Math.ceil(p.getTotalLength()) + 1;
          p.style.setProperty('--l', l + 'px');
        } catch (e) {}
      });
    }
    stampLengths();

    // 2. Intersection Observer to trigger storyboard on enter
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver(entries => {
        if (entries.some(e => e.isIntersecting)) {
          footer.classList.add('is-in');
          io.disconnect();
        }
      }, { threshold: 0.15 });
      io.observe(footer);
    } else {
      footer.classList.add('is-in');
    }

    // 3. Parallax tilt on mousemove
    footer.addEventListener('pointermove', e => {
      if (e.pointerType !== 'mouse') return;
      const r = footer.getBoundingClientRect();
      if (!r.width || !r.height) return;
      footer.style.setProperty('--ssf-px', (((e.clientX - r.left) / r.width - 0.5) * 2).toFixed(3));
      footer.style.setProperty('--ssf-py', (((e.clientY - r.top) / r.height - 0.5) * 2).toFixed(3));
    });
    footer.addEventListener('pointerleave', () => {
      footer.style.setProperty('--ssf-px', '0');
      footer.style.setProperty('--ssf-py', '0');
    });

    // 4. Interactive Draggable Stickers with Throw-Tilt & Slap Physics
    const stage = footer.querySelector('.ssf-stage-in');
    const stickers = footer.querySelectorAll('.ssf-st');
    let highestZ = 10;

    stickers.forEach((st) => {
      const btn = st.querySelector('.ssf-st-btn');
      const lift = st.querySelector('.ssf-st-lift');
      if (!btn) return;

      const homeX = parseFloat(st.dataset.homeX || st.style.left);
      const homeY = parseFloat(st.dataset.homeY || st.style.top);
      st.dataset.homeX = homeX;
      st.dataset.homeY = homeY;

      let drag = null;

      btn.addEventListener('pointerdown', e => {
        if (e.button !== 0 || !stage) return;
        const r = stage.getBoundingClientRect();
        btn.setPointerCapture(e.pointerId);
        highestZ++;
        st.style.zIndex = highestZ;

        drag = {
          id: e.pointerId,
          sx: parseFloat(st.style.left),
          sy: parseFloat(st.style.top),
          px: e.clientX,
          py: e.clientY,
          lx: e.clientX,
          t: performance.now(),
          tilt: 0,
          w: r.width,
          h: r.height,
          went: false
        };
      });

      btn.addEventListener('pointermove', e => {
        if (!drag || drag.id !== e.pointerId) return;
        const dx = e.clientX - drag.px;
        const dy = e.clientY - drag.py;
        if (!drag.went && Math.hypot(dx, dy) < 4) return;

        if (!drag.went) st.classList.add('is-drag');
        drag.went = true;

        const x = Math.min(99, Math.max(1, drag.sx + (dx / drag.w) * 100));
        const y = Math.min(96, Math.max(-70, drag.sy + (dy / drag.h) * 100));
        st.style.left = x + '%';
        st.style.top = y + '%';

        const now = performance.now();
        const v = (e.clientX - drag.lx) / Math.max(1, now - drag.t);
        drag.tilt = drag.tilt * 0.75 + Math.min(24, Math.max(-24, v * 22)) * 0.25;
        drag.lx = e.clientX;
        drag.t = now;
        st.style.setProperty('--tilt', drag.tilt.toFixed(2) + 'deg');
      });

      const onUp = e => {
        if (!drag || drag.id !== e.pointerId) return;
        drag = null;
        st.classList.remove('is-drag');
        st.style.setProperty('--tilt', '0deg');
        if (lift && lift.animate) {
          lift.animate([
            { transform: 'scale(1.14)' },
            { transform: 'scale(.93, 1.04)', offset: 0.4 },
            { transform: 'scale(1.02, .98)', offset: 0.7 },
            { transform: 'none' }
          ], { duration: 420, easing: 'cubic-bezier(.3, 1.4, .4, 1)' });
        }
      };

      btn.addEventListener('pointerup', onUp);
      btn.addEventListener('pointercancel', onUp);

      // Double-click returns sticker back to home position
      btn.addEventListener('dblclick', () => {
        st.style.left = homeX + '%';
        st.style.top = homeY + '%';
        if (lift && lift.animate) {
          lift.animate([
            { transform: 'scale(1.18)' },
            { transform: 'scale(.92, 1.05)', offset: 0.4 },
            { transform: 'none' }
          ], { duration: 420, easing: 'cubic-bezier(.3, 1.4, .4, 1)' });
        }
      });
    });

    // 5. Click wordmark to replay writing animation and send stickers home
    const wmBtn = footer.querySelector('.ssf-wm-btn');
    if (wmBtn) {
      wmBtn.addEventListener('click', () => {
        stickers.forEach(st => {
          st.style.left = st.dataset.homeX + '%';
          st.style.top = st.dataset.homeY + '%';
        });
        footer.classList.remove('is-in');
        void footer.offsetWidth; // force reflow
        stampLengths();
        footer.classList.add('is-in');
      });
    }

    // 6. Copy email on click
    const copyBtn = footer.querySelector('.ssf-copy');
    if (copyBtn) {
      copyBtn.addEventListener('click', async () => {
        const email = copyBtn.querySelector('.ssf-addr')?.textContent?.trim() || 'info@universityyatra.com';
        try {
          await navigator.clipboard.writeText(email);
          copyBtn.classList.add('is-copied');
          setTimeout(() => copyBtn.classList.remove('is-copied'), 2200);
        } catch (err) {
          window.location.href = 'mailto:' + email;
        }
      });
    }

    // 7. Credits popover toggle
    const creditsPill = footer.querySelector('.ssf-pill');
    const creditsPop = footer.querySelector('.ssf-pop');
    if (creditsPill && creditsPop) {
      creditsPill.addEventListener('click', e => {
        e.stopPropagation();
        creditsPop.style.display = creditsPop.style.display === 'block' ? 'none' : 'block';
      });
      document.addEventListener('pointerdown', e => {
        if (!creditsPop.contains(e.target) && e.target !== creditsPill) {
          creditsPop.style.display = 'none';
        }
      });
    }

    // 8. Seamless Dual-Buffer Video Looper (Eliminates flicker & loop pause)
    initSeamlessFooterVideo();
  }

  /* ========================================================
     STEALTH AMBIENT FOOTER VIDEO — SEAMLESS DUAL BUFFER LOOP
     Eliminates native browser loop-stall & black-frame flicker
     ======================================================== */
  function initSeamlessFooterVideo() {
    const vidA = document.getElementById('ssfVideoA');
    const vidB = document.getElementById('ssfVideoB');
    if (!vidA || !vidB) return;

    let isAActive = true;
    let isTransitioning = false;
    const CROSSFADE_OFFSET = 0.6; // Start crossfade 0.6s before video ends

    // Start playback safely with user gesture fallback for mobile
    const startPlay = () => {
      vidA.play().catch(() => {});
    };
    startPlay();
    document.addEventListener('touchstart', startPlay, { once: true, passive: true });
    document.addEventListener('click', startPlay, { once: true });

    // Monitor time of currently active video
    function checkCrossfade(activeVid, incomingVid) {
      if (isTransitioning) return;
      if (!activeVid.duration || isNaN(activeVid.duration)) return;

      const timeLeft = activeVid.duration - activeVid.currentTime;
      if (timeLeft <= CROSSFADE_OFFSET && timeLeft > 0) {
        isTransitioning = true;

        // Cue and play incoming video
        incomingVid.currentTime = 0;
        incomingVid.play().then(() => {
          incomingVid.classList.add('is-active');
          activeVid.classList.remove('is-active');

          setTimeout(() => {
            isAActive = !isAActive;
            isTransitioning = false;
          }, 650);
        }).catch(() => {
          isTransitioning = false;
        });
      }
    }

    vidA.addEventListener('timeupdate', () => {
      if (isAActive) checkCrossfade(vidA, vidB);
    });

    vidB.addEventListener('timeupdate', () => {
      if (!isAActive) checkCrossfade(vidB, vidA);
    });

    // Battery & CPU optimization: pause when off-screen
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            if (isAActive) vidA.play().catch(() => {});
            else vidB.play().catch(() => {});
          } else {
            vidA.pause();
            vidB.pause();
          }
        });
      }, { threshold: 0.1 });
      const footer = document.querySelector('.ssf');
      if (footer) observer.observe(footer);
    }
  }

  /* ========================================================
     SECTION 2 — STUDY PATHWAYS MOBILE CAROUSEL & AUTO-SWIPE
     ======================================================== */
  function initPathwaysSlider() {
    const grid = document.getElementById('pathwaysGrid');
    const sliderWrap = document.querySelector('.path-slider-wrap');
    const tabs = document.querySelectorAll('.path-tab-btn');
    const dots = document.querySelectorAll('.path-dot');
    const slides = document.querySelectorAll('.path-slide');
    if (!grid || slides.length < 2) return;

    let currentIndex = 0;
    let autoTimer = null;
    const INTERVAL_MS = 2800; // Set transition delay to under 3 seconds (2.8s auto-scroll)

    function goToSlide(index, restartTimer = true) {
      if (window.innerWidth > 768) {
        grid.style.transform = '';
        return;
      }

      currentIndex = (index + slides.length) % slides.length;
      grid.style.transform = 'translateX(-' + (currentIndex * 50) + '%)';

      // Update Tab Buttons
      tabs.forEach((tab, i) => {
        const isActive = i === currentIndex;
        tab.classList.toggle('is-active', isActive);
        tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });

      // Update Indicator Dots
      dots.forEach((dot, i) => {
        dot.classList.toggle('is-active', i === currentIndex);
      });

      // Update Slide State
      slides.forEach((slide, i) => {
        slide.classList.toggle('is-active', i === currentIndex);
      });

      if (restartTimer) {
        startTimer();
      }
    }

    function nextSlide() {
      goToSlide(currentIndex + 1, false);
    }

    function startTimer() {
      stopTimer();
      if (window.innerWidth <= 768) {
        autoTimer = setInterval(nextSlide, INTERVAL_MS);
      }
    }

    function stopTimer() {
      if (autoTimer) {
        clearInterval(autoTimer);
        autoTimer = null;
      }
    }

    // Tab Button Clicks
    tabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const idx = parseInt(tab.getAttribute('data-index'), 10) || 0;
        goToSlide(idx);
      });
    });

    // Dot Button Clicks
    dots.forEach(dot => {
      dot.addEventListener('click', () => {
        const idx = parseInt(dot.getAttribute('data-index'), 10) || 0;
        goToSlide(idx);
      });
    });

    // Touch Swipe Support
    let touchStartX = 0;
    let touchStartY = 0;
    let touchEndX = 0;
    let touchEndY = 0;

    const gestureTarget = sliderWrap || grid;

    gestureTarget.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
      stopTimer();
    }, { passive: true });

    gestureTarget.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      touchEndY = e.changedTouches[0].screenY;
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;

      if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 35) {
        if (diffX < 0) {
          goToSlide(currentIndex + 1);
        } else {
          goToSlide(currentIndex - 1);
        }
      } else {
        startTimer();
      }
    }, { passive: true });

    // Handle screen resize
    window.addEventListener('resize', () => {
      if (window.innerWidth > 768) {
        stopTimer();
        grid.style.transform = '';
      } else {
        goToSlide(currentIndex, true);
      }
    });

    // Initial setup on load
    if (window.innerWidth <= 768) {
      goToSlide(0, true);
    }
  }

  /* ==========================================================================
     REEL-STYLE STUDENT JOURNEY MODAL CONTROLLER (OPTION 1)
     ========================================================================== */
  function initStudentJourneyReelModal() {
    const modal = document.getElementById('uyReelModal');
    if (!modal) return;

    const backdrop = document.getElementById('uyReelBackdrop');
    const outerClose = document.getElementById('uyReelCloseBtn');
    const innerClose = document.getElementById('uyReelInnerClose');
    const intro = document.getElementById('uyReelIntro');
    const introTitle = document.getElementById('uyReelIntroTitle');
    const loaderBar = document.getElementById('uyReelLoaderBar');
    const video = document.getElementById('uyReelVideo');
    const centerPlay = document.getElementById('uyReelCenterPlay');
    const playPauseBtn = document.getElementById('uyReelPlayPause');
    const muteBtn = document.getElementById('uyReelMute');
    const track = document.getElementById('uyReelTrack');
    const trackFill = document.getElementById('uyReelTrackFill');
    const trackKnob = document.getElementById('uyReelTrackKnob');
    const timeText = document.getElementById('uyReelTime');
    const tag = document.getElementById('uyReelTag');

    const cards = document.querySelectorAll('.uy-card[data-story-video]');
    let introTimer = null;

    function formatTime(secs) {
      if (isNaN(secs) || secs < 0) return '0:00';
      const m = Math.floor(secs / 60);
      const s = Math.floor(secs % 60);
      return `${m}:${s < 10 ? '0' : ''}${s}`;
    }

    function openModal(name, videoSrc) {
      // 1. Set titles and video source
      if (introTitle) {
        introTitle.innerHTML = `${name}'s Story<br><span>Begins Like This...</span>`;
      }
      if (tag) {
        tag.innerHTML = `<i class="fa-solid fa-circle-play"></i> ${name}'s Journey`;
      }

      if (video) {
        video.src = videoSrc;
        video.load();
      }

      // 2. Reset intro state
      if (intro) {
        intro.classList.remove('is-hidden');
        intro.classList.add('is-animating');
      }
      if (loaderBar) {
        loaderBar.style.animation = 'none';
        void loaderBar.offsetHeight;
        loaderBar.style.animation = '';
      }

      // 3. Reset video controls state
      updatePlayPauseState(false);
      if (trackFill) trackFill.style.width = '0%';
      if (trackKnob) trackKnob.style.left = '0%';
      if (timeText) timeText.textContent = '0:00 / 0:00';

      // 4. Open modal
      modal.classList.add('is-active');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('uy-modal-open');

      if (introTimer) clearTimeout(introTimer);

      // 5. After intro animation (~1.4s), transition to video playback
      introTimer = setTimeout(() => {
        if (intro) {
          intro.classList.add('is-hidden');
          intro.classList.remove('is-animating');
        }
        if (video) {
          video.play().then(() => {
            updatePlayPauseState(true);
          }).catch(err => {
            console.warn('Auto-play prevented:', err);
            updatePlayPauseState(false);
            if (centerPlay) centerPlay.classList.add('is-visible');
          });
        }
      }, 1450);
    }

    function closeModal() {
      if (introTimer) clearTimeout(introTimer);
      if (video) {
        video.pause();
        video.currentTime = 0;
        video.src = '';
      }
      modal.classList.remove('is-active');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('uy-modal-open');
      if (intro) {
        intro.classList.remove('is-hidden', 'is-animating');
      }
      updatePlayPauseState(false);
    }

    function updatePlayPauseState(isPlaying) {
      if (playPauseBtn) {
        const icon = playPauseBtn.querySelector('i');
        if (icon) {
          icon.className = isPlaying ? 'fa-solid fa-pause' : 'fa-solid fa-play';
        }
      }
      if (centerPlay) {
        const centerIcon = centerPlay.querySelector('i');
        if (isPlaying) {
          centerPlay.classList.remove('is-visible');
          if (centerIcon) centerIcon.className = 'fa-solid fa-pause';
        } else {
          centerPlay.classList.add('is-visible');
          if (centerIcon) centerIcon.className = 'fa-solid fa-play';
        }
      }
    }

    function togglePlayPause() {
      if (!video) return;
      if (video.paused || video.ended) {
        if (video.ended) video.currentTime = 0;
        video.play().then(() => updatePlayPauseState(true)).catch(err => console.warn(err));
      } else {
        video.pause();
        updatePlayPauseState(false);
      }
    }

    // Attach click triggers to cards
    cards.forEach(card => {
      const visual = card.querySelector('.uy-visual');
      const name = card.dataset.storyName || 'Student';
      const videoSrc = card.dataset.storyVideo || '';

      function handleClick(e) {
        e.preventDefault();
        openModal(name, videoSrc);
      }

      if (visual) {
        visual.addEventListener('click', handleClick);
        visual.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleClick(e);
          }
        });
      }
    });

    // Close triggers
    if (backdrop) backdrop.addEventListener('click', closeModal);
    if (outerClose) outerClose.addEventListener('click', closeModal);
    if (innerClose) innerClose.addEventListener('click', closeModal);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('is-active')) {
        closeModal();
      }
    });

    // Play/Pause controls
    if (playPauseBtn) {
      playPauseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
    }
    if (centerPlay) {
      centerPlay.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
    }
    if (video) {
      video.addEventListener('click', (e) => {
        e.stopPropagation();
        togglePlayPause();
      });
      video.addEventListener('timeupdate', () => {
        if (!video.duration) return;
        const pct = Math.min(100, Math.max(0, (video.currentTime / video.duration) * 100));
        if (trackFill) trackFill.style.width = `${pct}%`;
        if (trackKnob) trackKnob.style.left = `${pct}%`;
        if (track) track.setAttribute('aria-valuenow', Math.round(pct));
        if (timeText) {
          timeText.textContent = `${formatTime(video.currentTime)} / ${formatTime(video.duration)}`;
        }
      });
      video.addEventListener('loadedmetadata', () => {
        if (timeText) {
          timeText.textContent = `0:00 / ${formatTime(video.duration)}`;
        }
      });
      video.addEventListener('ended', () => {
        updatePlayPauseState(false);
        if (centerPlay) {
          centerPlay.classList.add('is-visible');
          const centerIcon = centerPlay.querySelector('i');
          if (centerIcon) centerIcon.className = 'fa-solid fa-rotate-right';
        }
      });
      video.addEventListener('play', () => updatePlayPauseState(true));
      video.addEventListener('pause', () => updatePlayPauseState(false));
    }

    // Time scrubber
    if (track) {
      track.addEventListener('click', (e) => {
        e.stopPropagation();
        const rect = track.getBoundingClientRect();
        const clientX = e.clientX || (e.touches && e.touches[0] ? e.touches[0].clientX : 0);
        const pos = Math.min(Math.max(0, clientX - rect.left), rect.width);
        const fraction = pos / rect.width;
        if (video && video.duration) {
          video.currentTime = fraction * video.duration;
        }
      });
    }

    // Mute toggle
    if (muteBtn && video) {
      muteBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        video.muted = !video.muted;
        const icon = muteBtn.querySelector('i');
        if (icon) {
          icon.className = video.muted ? 'fa-solid fa-volume-xmark' : 'fa-solid fa-volume-high';
        }
      });
    }
  }

  /* ==========================================================================
     INLINE AUTOPLAY FOR STUDENT JOURNEY VIDEOS ON SCROLL
     ========================================================================== */
  function initInlineStudentAutoplay() {
    const section = document.getElementById('testimonials');
    if (!section) return;

    const grid = section.querySelector('.uy-grid');
    const inlineVideos = Array.from(section.querySelectorAll('.uy-inline-video'));
    const muteBtns = Array.from(section.querySelectorAll('.uy-inline-mute-btn'));
    if (!inlineVideos.length) return;

    let isInView = false;
    let activeMobileVid = inlineVideos[0];
    let isSoundOn = false;

    function syncMuteButtons() {
      muteBtns.forEach(btn => {
        const icon = btn.querySelector('i');
        if (icon) {
          icon.className = isSoundOn ? 'fa-solid fa-volume-high' : 'fa-solid fa-volume-xmark';
        }
        btn.setAttribute('aria-label', isSoundOn ? 'Mute video' : 'Unmute video');
      });
    }

    function checkSectionInView() {
      const rect = section.getBoundingClientRect();
      return rect.top < window.innerHeight * 0.92 && rect.bottom > window.innerHeight * 0.08;
    }

    // Keep .is-playing strictly synced with actual video playback state
    inlineVideos.forEach(vid => {
      const visual = vid.closest('.uy-visual');
      if (!visual) return;
      vid.addEventListener('playing', () => {
        if (!isMobileCarousel() || vid === activeMobileVid) {
          visual.classList.add('is-playing');
        }
      });
      vid.addEventListener('pause', () => {
        visual.classList.remove('is-playing');
      });
    });

    function playVideo(vid) {
      if (!vid || document.body.classList.contains('uy-modal-open')) return;
      const visual = vid.closest('.uy-visual');
      vid.playsInline = true;
      vid.muted = !isSoundOn;
      vid.defaultMuted = !isSoundOn;

      const attemptPlay = () => {
        const playPromise = vid.play();
        if (playPromise && typeof playPromise.then === 'function') {
          playPromise.then(() => {
            if (visual) visual.classList.add('is-playing');
          }).catch(() => {
            if (!vid.muted) {
              vid.muted = true;
              vid.defaultMuted = true;
              isSoundOn = false;
              syncMuteButtons();
              vid.play().then(() => {
                if (visual) visual.classList.add('is-playing');
              }).catch(() => {
                if (visual) visual.classList.remove('is-playing');
              });
            } else if (visual) {
              visual.classList.remove('is-playing');
            }
          });
        } else if (visual) {
          visual.classList.add('is-playing');
        }
      };

      if (vid.readyState < 2) {
        vid.addEventListener('canplay', () => {
          if (checkSectionInView() && !document.body.classList.contains('uy-modal-open')) {
            if (!isMobileCarousel() || vid === activeMobileVid) {
              attemptPlay();
            }
          }
        }, { once: true });
      }
      attemptPlay();
    }

    function pauseVideo(vid) {
      if (!vid) return;
      const visual = vid.closest('.uy-visual');
      vid.pause();
      vid.muted = true;
      if (visual) visual.classList.remove('is-playing');
    }

    function isMobileCarousel() {
      return window.innerWidth <= 640;
    }

    function syncActivePlayback() {
      isInView = checkSectionInView();
      if (!isInView || document.body.classList.contains('uy-modal-open')) {
        inlineVideos.forEach(pauseVideo);
        return;
      }
      if (isMobileCarousel()) {
        inlineVideos.forEach(vid => {
          if (vid === activeMobileVid) {
            if (vid.paused || !vid.closest('.uy-visual')?.classList.contains('is-playing')) {
              playVideo(vid);
            } else {
              vid.muted = !isSoundOn;
            }
          } else {
            pauseVideo(vid);
          }
        });
      } else {
        inlineVideos.forEach(vid => {
          if (vid.paused || !vid.closest('.uy-visual')?.classList.contains('is-playing')) {
            playVideo(vid);
          } else {
            vid.muted = !isSoundOn;
          }
        });
      }
    }

    function pauseAll() {
      inlineVideos.forEach(pauseVideo);
    }

    // Inline Volume (Mute/Unmute) buttons
    muteBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const visual = btn.closest('.uy-visual');
        const vid = visual ? visual.querySelector('.uy-inline-video') : null;
        isSoundOn = !isSoundOn;
        syncMuteButtons();
        if (vid) {
          vid.muted = !isSoundOn;
          if (vid.paused) {
            playVideo(vid);
          }
        }
      });
    });
    syncMuteButtons();

    // Track horizontal swipe + touch unlock so mobile browsers NEVER block video playback
    if (grid) {
      let touchStartX = 0;
      let videosUnlocked = false;

      const unlockVideosOnGesture = () => {
        if (videosUnlocked) return;
        videosUnlocked = true;
        inlineVideos.forEach(v => {
          v.playsInline = true;
          v.muted = !isSoundOn;
          const p = v.play();
          if (p && typeof p.then === 'function') {
            p.then(() => {
              if (isMobileCarousel() && v !== activeMobileVid) {
                v.pause();
                const vis = v.closest('.uy-visual');
                if (vis) vis.classList.remove('is-playing');
              }
            }).catch(() => {});
          }
        });
      };

      const updateActiveOnScroll = () => {
        if (!isMobileCarousel()) return;
        const gridRect = grid.getBoundingClientRect();
        const gridCenter = gridRect.left + gridRect.width / 2;
        let bestVid = activeMobileVid;
        let bestDist = Infinity;

        inlineVideos.forEach(vid => {
          const card = vid.closest('.uy-card');
          if (!card) return;
          const r = card.getBoundingClientRect();
          const cardCenter = r.left + r.width / 2;
          const dist = Math.abs(cardCenter - gridCenter);
          if (dist < bestDist) {
            bestDist = dist;
            bestVid = vid;
          }
        });

        activeMobileVid = bestVid;
        syncActivePlayback();
      };

      grid.addEventListener('touchstart', (e) => {
        if (e.touches && e.touches[0]) {
          touchStartX = e.touches[0].clientX;
        }
        unlockVideosOnGesture();
      }, { passive: true });

      grid.addEventListener('touchend', (e) => {
        if (!isMobileCarousel()) return;
        const endX = (e.changedTouches && e.changedTouches[0]) ? e.changedTouches[0].clientX : touchStartX;
        const deltaX = endX - touchStartX;
        const currentIdx = inlineVideos.indexOf(activeMobileVid);
        if (deltaX < -30 && currentIdx < inlineVideos.length - 1) {
          activeMobileVid = inlineVideos[currentIdx + 1];
        } else if (deltaX > 30 && currentIdx > 0) {
          activeMobileVid = inlineVideos[currentIdx - 1];
        }
        // Call synchronously inside touchend so browser treats it as a direct user gesture
        syncActivePlayback();
        setTimeout(updateActiveOnScroll, 180);
      }, { passive: true });

      if ('IntersectionObserver' in window) {
        const cardObserver = new IntersectionObserver((entries) => {
          if (!isMobileCarousel()) return;
          entries.forEach(entry => {
            if (entry.isIntersecting && entry.intersectionRatio >= 0.55) {
              const vid = entry.target.querySelector('.uy-inline-video');
              if (vid) {
                activeMobileVid = vid;
                syncActivePlayback();
              }
            }
          });
        }, { root: grid, threshold: [0.55, 0.75] });

        section.querySelectorAll('.uy-card').forEach(card => cardObserver.observe(card));
      }

      let scrollTimer = null;
      grid.addEventListener('scroll', () => {
        if (scrollTimer) clearTimeout(scrollTimer);
        scrollTimer = setTimeout(updateActiveOnScroll, 60);
      }, { passive: true });
      if ('onscrollend' in grid) {
        grid.addEventListener('scrollend', updateActiveOnScroll, { passive: true });
      }
    }

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          isInView = entry.isIntersecting;
          syncActivePlayback();
        });
      }, { threshold: 0.15 });
      observer.observe(section);
    } else {
      isInView = true;
      syncActivePlayback();
    }

    window.addEventListener('scroll', () => {
      if (checkSectionInView() !== isInView) {
        syncActivePlayback();
      }
    }, { passive: true });
    window.addEventListener('resize', syncActivePlayback);
    window.addEventListener('pointerdown', syncActivePlayback, { once: true, passive: true });

    // Pause inline videos when modal opens; resume when closed if still in view
    const modal = document.getElementById('uyReelModal');
    if (modal && 'MutationObserver' in window) {
      const modalObserver = new MutationObserver(() => {
        if (modal.classList.contains('is-active')) {
          pauseAll();
        } else if (isInView) {
          syncActivePlayback();
        }
      });
      modalObserver.observe(modal, { attributes: true, attributeFilter: ['class'] });
    }
  }

  // Alias
  function initTestimonialsStories() {
    initStudentJourneyReelModal();
    initInlineStudentAutoplay();
  }

  /* =====================================================
     HERO 3-FRIENDS CHAT CONTROLLER
     Infinite loop conversational speech bubbles directly above speakers
     ===================================================== */
  function initHeroDialogue() {
    const stage = document.getElementById('heroDialogueStage');
    if (!stage) return;

    const bubble3 = document.getElementById('bubbleSpeaker3');
    const bubble1 = document.getElementById('bubbleSpeaker1');
    const bubble2 = document.getElementById('bubbleSpeaker2');

    const text3 = document.getElementById('bubbleText3');
    const text1 = document.getElementById('bubbleText1');
    const text2 = document.getElementById('bubbleText2');

    if (!bubble3 || !bubble1 || !bubble2) return;

    // The 9 dialogue lines requested by the user:
    // Speaker 1: Middle girl (purple sweater)
    // Speaker 2: Right boy (green jacket)
    // Speaker 3: Left boy (glasses & headphones - guide)
    const DIALOGUE = [
      { speaker: 1, text: 'Fast Track abroad?', duration: 2400 },
      { speaker: 2, text: 'How does it work?', duration: 2400 },
      { speaker: 3, text: 'Start online in India.', duration: 2600 },
      { speaker: 1, text: 'For 8–12 months?', duration: 2400 },
      { speaker: 3, text: 'Then transfer abroad.', duration: 2600 },
      { speaker: 2, text: 'Lower study costs?', duration: 2400 },
      { speaker: 3, text: 'Save up to 50%*.', duration: 2600 },
      { speaker: 1, text: 'Who can guide us?', duration: 2400 },
      { speaker: 3, text: 'University Yatra', duration: 3400, isHighlight: true }
    ];

    let currentIndex = 0;
    let timer = null;
    let isPaused = false;

    function renderStep(index) {
      const item = DIALOGUE[index];

      // Deactivate all bubbles first
      bubble1.classList.remove('is-active');
      bubble2.classList.remove('is-active');
      bubble3.classList.remove('is-active', 'is-brand-highlight');

      requestAnimationFrame(() => {
        if (item.speaker === 1) {
          if (text1) text1.textContent = item.text;
          bubble1.classList.add('is-active');
        } else if (item.speaker === 2) {
          if (text2) text2.textContent = item.text;
          bubble2.classList.add('is-active');
        } else if (item.speaker === 3) {
          if (text3) text3.textContent = item.text;
          if (item.isHighlight) {
            bubble3.classList.add('is-brand-highlight');
          }
          bubble3.classList.add('is-active');
        }
      });
    }

    function scheduleNext() {
      if (timer) clearTimeout(timer);
      const currentItem = DIALOGUE[currentIndex];
      const duration = currentItem.duration || 2400;

      timer = setTimeout(() => {
        if (isPaused) return;
        currentIndex++;
        if (currentIndex >= DIALOGUE.length) {
          // Loop reset: fade out last message, pause gently, then start from beginning
          bubble1.classList.remove('is-active');
          bubble2.classList.remove('is-active');
          bubble3.classList.remove('is-active', 'is-brand-highlight');

          currentIndex = 0;
          timer = setTimeout(() => {
            if (!isPaused) {
              renderStep(currentIndex);
              scheduleNext();
            }
          }, 450);
        } else {
          renderStep(currentIndex);
          scheduleNext();
        }
      }, duration);
    }

    // Tap/click anywhere on stage to advance conversation immediately
    stage.addEventListener('click', () => {
      if (timer) clearTimeout(timer);
      currentIndex = (currentIndex + 1) % DIALOGUE.length;
      renderStep(currentIndex);
      scheduleNext();
    });

    // Handle tab visibility to avoid queuing animations
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        isPaused = true;
        if (timer) clearTimeout(timer);
      } else {
        isPaused = false;
        renderStep(currentIndex);
        scheduleNext();
      }
    });

    // Initial trigger
    renderStep(0);
    scheduleNext();
  }

  /* =====================================================
     SCROLL DIRECTION CONTROLLER
     Hide header (University Yatra) & Bottom Bar (WhatsApp CTA) on scroll-up & scroll-down
     Reveal at top of page
     ===================================================== */
  function initScrollDirectionBars() {
    let ticking = false;

    const updateBars = () => {
      const currentScrollY = window.pageYOffset || document.documentElement.scrollTop || 0;
      if (currentScrollY <= 20) {
        // At top of page
        document.body.classList.remove('scroll-down', 'header-hidden');
      } else {
        // Scrolled past top -> hide header & bottom WhatsApp CTA bar
        document.body.classList.add('scroll-down', 'header-hidden');
      }
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateBars);
        ticking = true;
      }
    }, { passive: true });
    updateBars();
  }

  function initFooterLegalToggle() {
    const btn = document.getElementById('footerSeeMoreBtn');
    const disclaimer = document.getElementById('footerLegalDisclaimer');
    if (!btn || !disclaimer) return;

    const label = btn.querySelector('.footer-seemore-label');
    btn.addEventListener('click', () => {
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      const nextState = !isExpanded;
      btn.setAttribute('aria-expanded', String(nextState));
      disclaimer.hidden = !nextState;
      if (label) {
        label.textContent = nextState ? '( see less )' : '( see more )';
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initWizardController();
    initBottomEnquiry();
    initStickerSlapFooter();
    initPathwaysSlider();
    initTestimonialsStories();
    initHeroDialogue();
    initScrollDirectionBars();
    initFooterLegalToggle();
  });

})();
