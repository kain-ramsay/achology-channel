# REPORT: the complete live copy of all seven policy pages

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `BRIEF__Report_Live_Policy_Copy_All_Seven_Pages.md`.
**Read only. Nothing was edited, nothing published, nothing changed on the site.**

**This file deliberately contains em and en dashes, and the dash gate will flag it.** You asked for the copy verbatim, and the dashes are in the live copy; tidying them here would poison the mirror, which is exactly what you warned against. Every dash below is quoted, none is mine.

## Where these words come from, and why that matters

All seven pages keep their WordPress editor empty. The words a visitor reads are baked into the theme, one file per page, under `achology/policies-content/`, rendered through `template-policy.php`. So the theme is the source of truth for the copy, and WordPress holds only the page's title and address.

Rather than read those PHP files, I fetched each published page from inside the server and extracted the rendered text, because that is literally what a visitor sees, entities resolved and all. Every page below therefore carries **the deployed output, not the source file**. The two should agree; reading the output is what proves they do.

Everything between the page title and the closing note is included, in order. The closing note itself ("Questions about this policy? Get in touch with our support team") is the template's, identical on all seven, and is not repeated per page below.

**Every page displays the same last updated date: 1 July 2026.** That date is baked into each content file. As far as I can tell from the theme's history it is a written date rather than a generated one, so it reflects when the copy was written, not the last time the file changed. Several files have been touched since for structural work; none of the wording changed, so the displayed date is still honest.

## Observations, listed only, nothing fixed

**1. The dash ban is broken on six of the seven pages, and worse than a source search suggests.** In the rendered text: privacy policy 42 em dashes, cookie policy 19, terms and conditions 11, trust statement 11, accessibility statement 5, disclaimers 3 em plus 3 en. The refund policy is clean. Most are written in the source as the HTML entity rather than the character, so a search of the files for the character alone finds only a handful and reads as almost clean. It is not: search the rendered page, or search for the entity too.

**2. No canonical tag on any of the seven.** Already known, already ruled Rank Math configuration rather than a page defect.

**3. Structurally the seven are at standard**, as of the page_gate map filed today: hairlines present, 48 above and below at desktop and tablet, 32 on phone, widths, gutters and H1 all correct, every asset loading, every link resolving.

**4. Terms and Conditions carries 33 headings across 2,855 words**, the densest of the seven. Not a defect against any written standard, noted because it affects how the vault note will read.

---

# Terms and Conditions

**Live URL:** https://achologytest.com/policies/terms-and-conditions/
**Source read:** the deployed page output, supplied by `achology/policies-content/terms-and-conditions.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 2855 words.

## Body copy, verbatim

## Definitions Used Throughout Our Policies

“Achology”, “we”, “us”, “our” — Achology Transactions Ltd.

“You”, “your” — The individual purchasing or accessing the products.

“Products” — All digital courses, course bundles, subscriptions, events, learning materials, and services supplied by Achology.

“Digital Content” — Any content supplied in digital form, including video, audio, text, downloadable materials, and platform access.

“Community” / “Community Platform” — Achology’s online learning and discussion environment, including peer interaction spaces.

“Subscription” — Any recurring or time-limited access product, including Community subscriptions.

“Certification” / “Achology Practitioner Certification” — Educational recognition awarded within Achology’s framework only, not a licence or statutory qualification.

“Practice Events” — Peer-based learning activities where members practise coaching or helping skills.

“Terms” — These Terms & Conditions as updated from time to time.

## 1. Who We Are and How to Contact Us

Who we are: Achology is the trading name of Achology Transactions Ltd (ATL) — Scottish company number SC697126 — based in Glasgow, Scotland.

Our registered office is at:

Clyde Offices, 2nd Floor, 48 West George Street, Glasgow, Scotland, G2 1BP.

Contacting us: You can contact our customer support team by telephone on +44 (0)1383 344 086 or by email at support@achology.com.

Where necessary, we may contact you by telephone, email, or post using the contact details you provide when placing an order.

## 2. Our Contract With You

Your order: When you purchase access to courses (individually or as part of a bundle), your contract is with Achology Transactions Ltd (ATL).

Community subscriptions are likewise contracts with Achology Transactions Ltd (ATL).

By placing an order, you make an offer to enter into a contract with Achology Transactions Ltd on these Terms. A legally binding contract is formed when we send you an email confirming acceptance of your order.

We reserve the right to decline any order at our discretion. If we decline an order, we will:

- notify you by email; and

- not take payment, or promptly refund any payment already taken in relation to that order.

## 3. Courses, Certificate Programmes, and Subscriptions

When you place an order, the order page will specify the materials included, the length of access (where applicable), and the price payable. These details form part of your agreement with us, and you should review them carefully before completing your purchase.

Some products offer the opportunity to work towards Achology Practitioner certification. Achology may create, amend, or withdraw qualifications, and may set or revise ongoing education or maintenance requirements, by providing reasonable notice through our website or platform.

Achology certifications reflect educational achievement within our framework only and do not confer legal or professional authority outside of it.

### Memberships renew automatically

Achology Membership is a renewing subscription. The monthly plan is $7 for the first 30 days and then the standard monthly rate (currently $34.50 per month); the annual plan is $345 per year and renews each year unless you cancel before the renewal date. You can cancel at any time inside the community platform (Circle.io), which stops all future payments.

When you buy a course, you also receive 3 months of complimentary Achology Membership. After those 3 months, membership continues at the standard monthly rate (currently $34.50 per month) until you cancel. Refunding a course does not, by itself, cancel that membership; if you do not wish it to continue, cancel it separately. Full details are in our Refunds Policy.

## 4. Prohibition on Recording or Sharing Content

Each purchase grants access for one individual only, unless the product description expressly states otherwise. The fees you pay permit a single user to access and use the course materials for personal, non-transferable use.

You must keep your account details confidential and must not share, transfer, or allow access to your account by any other person.

You must not copy, record, download, reproduce, distribute, share, sell, sublicense, or rebroadcast any course materials, in whole or in part, in any format or medium, whether for commercial or non-commercial purposes, without our prior written permission.

## 5. The Community Blog (Posts)

Members of our online community may submit articles for consideration for publication on our community blog. We reserve the right, at our sole discretion, to decide whether to publish any submission and to remove or withdraw a published post at any time, with or without notice.

You must only submit content that is original to you and that you have the full right to submit for publication. You must not submit content that infringes the intellectual property rights or other rights of any third party. If a submission you provide results in a claim, demand, or legal action against us, you agree to be responsible for any reasonable losses, costs, or expenses we incur as a result.

By submitting an article for publication, you grant us a perpetual, royalty-free, non-exclusive, non-transferable, and irrevocable licence to reproduce, display, and make the article available on our website and associated platforms. You also grant us permission to format, edit, and adapt the submission for clarity, spelling, grammar, layout, and alignment with the tone and style of our website.

We will not materially alter the meaning or intent of your submission without your consent.

## 6. Your Rights to Make Changes

If you wish to change the product you have ordered, please contact us as soon as possible. We will let you know whether the requested change is available and whether it would result in any adjustment to the price payable.

We are not obliged to agree to changes. If a requested change is not available, or if you do not wish to proceed on the revised terms offered, you may choose to end the contract in accordance with clause 8 (Your Rights to End the Contract).

## 7. Our Rights to Change These Terms and Conditions or Our Programmes

Minor changes: We may make minor changes to these Terms or to the features of our products where such changes are necessary to:

- comply with changes in applicable law or regulatory requirements; or

- implement technical adjustments or improvements, including to improve functionality, reliability, performance, or to address security issues.

Minor changes will not materially affect your access to purchased content or the overall nature of the services provided.

More significant changes: We may also make more significant changes to our programmes, including by:

- updating, revising, or replacing course content;

- changing the availability, structure, or delivery of courses; or

- changing, replacing, or discontinuing certification or certificate programmes.

Where a more significant change materially affects your access to, or use of, a programme you have already purchased, we will provide reasonable notice and explain your options, which may include the right to end the contract in accordance with these Terms.

## 8. Your Rights to End the Contract

You may end your contract with us at any time. Your rights when ending the contract will depend on the circumstances and the reason for cancellation. An example cancellation notice is provided in Schedule 1 for your convenience, although you are not required to use this wording.

### Digital content and your statutory cooling-off right

All of our products are digital content, supplied to you immediately once your purchase completes. By completing checkout you expressly consent to that immediate supply, and you acknowledge that in giving that consent you lose the statutory 14-day right to cancel that the Consumer Contracts Regulations 2013 would otherwise give you.

For every product except Community subscriptions, our own 14-day money-back guarantee below matches the length of that right and is simpler to use. For Community subscriptions, access begins the moment you join and, as set out below, they are non-refundable once access is granted, though you may cancel at any time to stop future payments.

### Our 14-day money-back guarantee

We offer a full 14-day money-back guarantee on all products except community membership. This covers all individual courses, course bundles, and the Access All Areas Pass.

If you decide within 14 days of purchase that a product is not right for you, you may ask for a full refund. You do not need to provide a reason, and we will not dispute your decision. We may invite feedback to help us improve our offerings, but your feedback is optional.

This 14-day guarantee does not apply to Community subscriptions. Once access has been granted, Community subscriptions are non-refundable, although you may cancel at any time to prevent future payments.

### Other situations where you are entitled to a full refund

You may also end the contract and receive a full refund if:

- there is a material error in the price or description of the product you ordered; or

- we suspend access to the purchased products for technical reasons for a continuous period of 7 days or more.

### How to end the contract with us

To cancel your contract or request a refund, please contact us using one of the following methods:

- Telephone: +44 (0)1383 344 086

- Email: support@achology.com

- Website: by completing our contact form

## 9. Our Rights to End the Contract

We may end this contract if you materially breach these Terms, including where you:

- fail to make a payment when it is due and do not remedy that failure within 14 days of us notifying you that the payment is overdue; or

- breach clause 4 (Prohibition on Recording or Sharing Content).

We may suspend your access to any subscription-based service if a payment method you have provided is invalid, declined, or otherwise fails. Access may remain suspended until valid payment details are provided and any outstanding amounts are paid.

We may withdraw or terminate your access to a subscription service if your behaviour in our community spaces endangers or exploits others (predatory conduct, harassment, or unlawful activity), the boundary set out in our Trust Statement. In such cases, withdrawal of access may be immediate and does not require prior notice where the behaviour is serious or repeated.

## 10. Achology Refunds Policy

Our Refunds Policy forms part of these Terms & Conditions.

It sets out the circumstances in which refunds may be available, the products to which refunds apply, and the situations in which refunds are not offered. By placing an order, you confirm that you have read, understood, and agreed to the Refunds Policy in addition to these Terms.

In the event of any inconsistency between these Terms and the Refunds Policy, these Terms shall prevail, except where consumer law requires otherwise.

## 11. Summary of Your Legal Rights

We are legally required to supply products that comply with this contract. Nothing in these Terms limits or removes your statutory consumer rights.

The summary below outlines your legal rights regarding our products. These rights apply in addition to any other rights available to you under law.

These are your key legal rights:

All products supplied by us are treated as digital content. Under the Consumer Rights Act 2015, digital content must:

- be as described;

- be fit for purpose; and

- be of satisfactory quality.

If the digital content we provide is faulty, you are entitled to a repair or replacement.

If the fault cannot be fixed, or is not fixed within a reasonable time and without significant inconvenience, you may be entitled to a full or partial refund.

If you can demonstrate that faulty digital content has caused damage to your device, and we did not exercise reasonable care and skill, you may be entitled to a repair or compensation.

These rights are subject to certain conditions and exceptions set out in law.

For independent guidance on your statutory rights, you can contact Citizens Advice or visit their website.

## 12. Our Liability to You

Achology is not responsible for your devices or for maintaining their functionality, security, or compatibility with our digital content.

We will only be responsible for damage to your device or other digital content where such damage is directly caused by our failure to exercise reasonable care and skill in creating or supplying the digital content, as required by law. Where this applies, we will either repair the damage or provide appropriate compensation.

We are not responsible for any damage that:

- could have been avoided by following our instructions or advice, including installing updates or fixes made available to you free of charge;

- results from incorrect installation, misuse, or failure to follow usage instructions; or

- arises because your device does not meet the minimum technical or system requirements we specify for using the digital content.

### Business losses

Our products are provided for personal and educational use only. We are not liable for business-related losses, including loss of profit, loss of business, business interruption, or loss of business opportunity, even if such losses arise from your use of our products.

### Practice coaching and peer-based activities

Some Achology practice events involve members meeting with other members or non-members to practise coaching or helping skills. These sessions are practice-only learning activities.

We do not assess, supervise, endorse, or guarantee the quality, suitability, or outcomes of coaching or guidance you may receive from other participants. You take full responsibility for choosing whether to participate and for any coaching, feedback, or guidance you accept from others during these practice activities.

## 13. Other Important and Notable Terms

### Transfer of this agreement

We may transfer our rights and obligations under this contract to another organisation. If we do so, we will notify you in writing and ensure that the transfer does not adversely affect your rights under this contract.

You may not transfer your rights or obligations under this contract to any other person. All products and services are provided for the personal use of the purchaser only.

### Third-party rights

This contract is between you and us only. No other person has any rights to enforce any term of this contract under the Contracts (Rights of Third Parties) Act 1999 or otherwise.

### Governing law and jurisdiction

These Terms are governed by Scots law.

If you live in the United Kingdom, any dispute arising out of or in connection with this contract must be brought before the courts of the part of the UK in which you live.

If you live outside the United Kingdom, any dispute arising out of or in connection with this contract must be brought before the Scottish courts, which shall have exclusive jurisdiction.

### Model Cancellation Form (Schedule 1)

(Complete and return this form only if you wish to withdraw from the contract.)

To: Achology Transactions Ltd Clyde Offices, 2nd Floor, 48 West George Street, Glasgow, Scotland, G2 1BP Email: support@achology.com Telephone: +44 (0)1383 344 086

I/we hereby give notice that I/we cancel my/our contract for the supply of the following digital content or services:

- Ordered on / received on:

- Name of consumer(s):

- Address of consumer(s):

- Signature of consumer(s) (only required if submitted in paper form):

- Date:

## 14. Final Provisions

### Severability

If any part of these Terms is found to be unlawful, invalid, or unenforceable by a court or competent authority, that part will be deemed removed to the minimum extent necessary. The remainder of the Terms will continue in full force and effect.

### Waiver

If we do not enforce a particular right or provision under these Terms, this does not mean we have waived our right to do so in the future. Any waiver must be expressly agreed by us in writing to be effective.

### Entire agreement

These Terms, together with any documents expressly referred to within them (including our Trust Statement and Disclaimers), constitute the entire agreement between you and us in relation to your purchase and use of our products.

They replace and supersede any prior agreements, understandings, or communications, whether written or oral, relating to the same subject matter.

### No reliance on representations

You acknowledge that, in entering into this contract, you have not relied on any statement, promise, or representation that is not expressly set out in these Terms or in documents expressly incorporated by reference.

Nothing in this clause limits or excludes liability for fraudulent misrepresentation.

### Force majeure

We will not be liable for any delay or failure to perform our obligations under these Terms where such delay or failure results from events beyond our reasonable control. This includes, but is not limited to, interruptions to internet services, platform outages, power failures, acts of government, natural events, or other circumstances outside our reasonable control.

### How to contact us

If you have questions about these Terms, your contract, or your rights, you can contact us using the details set out in the “Who We Are and How to Contact Us” section of these Terms.

### Updates to these Terms

We may update these Terms from time to time in accordance with the provisions set out above. The version in force at the time you place your order will apply to that purchase, unless changes are required by law or are otherwise permitted under these Terms.

Our Trust Statement and Disclaimers form part of the context in which these Terms operate.

---

# Privacy Policy

**Live URL:** https://achologytest.com/policies/privacy-policy/
**Source read:** the deployed page output, supplied by `achology/policies-content/privacy-policy.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 4162 words.

## Body copy, verbatim

## How We Handle Personal Data

This Privacy Policy explains how Achology collects, uses, stores, and protects personal data in accordance with the UK General Data Protection Regulation (UK GDPR), the Data Protection Act 2018, and, where applicable, the EU General Data Protection Regulation (EU GDPR) and the Privacy and Electronic Communications Regulations 2003 (PECR).

Achology is the trading name of Achology Transactions Ltd. Throughout this Privacy Policy, references to “Achology”, “we”, “us”, or “our” refer to Achology Transactions Ltd, the entity responsible for processing your personal data.

We process personal data relating to members of our learning community, event attendees, customers, suppliers, employees, and other individuals who interact with Achology. We are committed to handling personal data lawfully, fairly, and transparently, and to collecting only the information that is necessary for legitimate and clearly defined purposes.

Where personal data is provided through surveys or similar activities, this will generally be limited to basic contact details unless otherwise stated. Individuals are responsible for ensuring that the information they provide is accurate and up to date.

In some circumstances, personal data may be transferred or accessed outside your country of residence. Where this occurs, we ensure that appropriate safeguards are in place to protect your data in line with applicable data protection laws.

Some Achology events may be recorded for educational or access purposes. Where recording takes place, this will be done in a proportionate manner and in accordance with this Privacy Policy.

This Privacy Policy sets out our lawful bases for processing personal data, how your data is protected, and the rights available to you. A copy of this Privacy Policy is available on this website and can also be provided on request.

## 1. Full Privacy Policy

Achology Transactions Ltd (Scottish company number SC697126) operates under the trading name Achology. When providing our courses, certifications, communications, and community platforms, we collect and process personal data. For the purposes of data protection law, Achology acts as a Data Controller in relation to that personal data.

We are responsible for ensuring that personal data is processed lawfully, fairly, and transparently, and in compliance with the UK General Data Protection Regulation (UK GDPR), the Data Protection Act 2018, and any other applicable data protection legislation.

This Privacy Policy explains what personal data we collect, how and why it is used, how it is protected, and the rights available to individuals whose personal data we process.

Our services and content are designed for adults aged 18 and over. We do not knowingly collect personal data from children. If you believe a child has provided us with personal data, please contact us using the details in section 2 and we will delete it.

## 2. Our Contact Details

Achology Transactions Ltd Clyde Offices, 2nd Floor 48 West George Street Glasgow, Scotland G2 1BP United Kingdom

Email: support@achology.com

If you have any questions about this Privacy Policy, or about how your personal data is collected, used, or protected, you can contact us using the details above or through our contact form.

## 3. What Personal Data Does Achology Collect and Process?

Depending on how you interact with Achology, we may collect and process the following categories of personal data:

Contact information — Your name, postal address, email address, and telephone number.

Account and registration details — Login credentials, user profile information, and account activity associated with your use of our platforms.

Transaction and service information — Details of products and services provided to you, including courses purchased, events attended, certifications awarded, credits earned, and related learning activity.

Communications — Records of correspondence between you and Achology, including emails, support enquiries, and other communications.

Images and recordings — Photographs, video, or audio recordings captured during events or learning activities where recording is taking place and participants have been informed.

Technical and usage data — Information collected through cookies and similar technologies, including device information, browser data, and interaction with our website or platforms. Further details are set out in our Cookie Policy.

Marketing and communication preferences — Your preferences regarding the receipt of marketing communications and updates from Achology.

Financial information — Payment-related details required to process transactions. Payment data is handled securely and, where applicable, processed by third-party payment providers rather than stored directly by us.

Recruitment-related information — Where you apply for a role with Achology, we may process employment history, education history, and other information relevant to the recruitment process.

Business or professional information — Information relating to your business activities, professional interests, or areas of study, where relevant to the services provided.

## 4. Special Categories of Personal Data

Achology does not intentionally collect, process, or store special categories of personal data (as defined under UK GDPR), such as data relating to health, racial or ethnic origin, religious or philosophical beliefs, political opinions, trade union membership, genetic data, biometric data, or sexual orientation.

If such information is disclosed to us inadvertently or voluntarily outside of any request by Achology (for example, within open text fields or community discussions), it will not be used for any specific purpose and will be handled in accordance with this Privacy Policy and applicable data protection law.

## 5. How We Collect Your Information

In most cases, we collect personal data directly from you when you interact with Achology. This includes situations where you:

- complete an online contact or enquiry form;

- register an account on achology.com or subscribe to our mailing list;

- generate course certificates or credits using our systems;

- register for, attend, or participate in events;

- join or participate in our community platforms;

- post, upload, or submit content (including articles or blog posts) within the community;

- communicate with us by email, post, or during meetings or discussions about our services or a contract with you;

- sign up for newsletters or service-related communications.

### Employment and recruitment

When you apply for employment or engagement with Achology, we may collect personal data when you:

- submit a CV or application materials; or

- provide information relevant to an employment or contractual relationship.

### Information collected from third parties

In some circumstances, we may receive personal data indirectly from third-party sources, including:

- third-party marketplaces or platforms through which you have purchased Achology courses or events;

- social media platforms (such as LinkedIn), where you interact with Achology in a professional context;

- publicly available sources, including limited demographic or market research data; or

- organisations that nominate you as an event attendee or point of contact.

### Information about other individuals

Where you provide personal data relating to another individual (for example, by nominating a contact or event attendee), you are responsible for ensuring that you have the appropriate authority to do so and that the individual has been made aware of this Privacy Policy.

### Data minimisation and account responsibility

We do not seek to collect personal data beyond what is necessary for the purposes described in this Privacy Policy. Where you choose to add, update, or modify information within your account, you are responsible for reviewing and managing your privacy settings accordingly.

## 6. Why We Collect and Use Your Personal Data

Where Achology collects and processes personal data, we do so for specific, legitimate purposes and only where there is a lawful basis under the UK General Data Protection Regulation (UK GDPR).

Depending on the circumstances, the lawful bases we rely on include:

- Contractual necessity — where processing is required to provide services you have requested, to deliver courses, subscriptions, certifications, or to manage your account.

- Legal obligation — where processing is required to meet legal, regulatory, or reporting requirements.

- Legitimate interests — where processing is necessary for the operation, security, improvement, and administration of our educational services, provided those interests are not overridden by your rights and freedoms.

- Consent — where required by law, such as for certain marketing communications or non-essential cookies.

- Vital interests or public interest — only in rare and exceptional circumstances where required by law.

We avoid relying on consent when another lawful basis is more suitable, and we only process personal data when there is a justified purpose.

The purposes for which we process personal data, and the lawful basis for each, are set out below:

| Our purpose for processing | Our legal basis |

| To understand your requirements prior to entering into a contract with you to complete or attend a course or event | The processing is necessary for the performance of an anticipated contract |

| To fulfil our contract with you and provide you with the agreed course and content therein | The processing is necessary for the performance of our contract with you |

| To manage our business operations and comply with any internal policies and procedures | It is in our legitimate interests to use your personal information to ensure that we continually improve and adapt our services |

| To notify you about updates and changes to our service | It is in our legitimate interests to use your personal information to keep you informed about any changes that may affect you |

| For email marketing of similar events and courses to existing or previous customers | It is in our legitimate interests to use your personal information for marketing purposes where the services being marketed are relevant to you |

| For newsletters and promotions to individuals who sign up to our mailing list | When you agree to join our mailing list by selecting this option when visiting our website, forums, or courses, we rely on your consent |

| For electronic marketing of services to new customers via personal business email addresses | It is in our legitimate interests to use personal business email addresses for marketing purposes where we can support individual rights |

| For electronic marketing of services to new individuals | We rely on consent for direct marketing to previously unknown individuals, including those who sign up to receive our newsletter |

| To comply with our legal obligations, law enforcement, court, and regulatory bodies’ requirements | To comply with our legal obligations |

| To identify and prevent fraud | It is in our legitimate interests to act as a responsible business |

| To decide whether to enter into a contract of employment or supplier services with you | The processing is necessary when considering a contract |

| To carry out background and reference checks in relation to recruitment | The processing is necessary when considering an employment contract |

| To communicate with you about a potential or existing contract (for service or employment) | The processing is necessary for the performance of, and compliance with, any contract of employment |

| To manage payroll and employment services for existing employees | The processing is necessary for the performance of, and compliance with, any contract of employment |

Where we rely on your consent, you have the right to withdraw this consent at any time by contacting us using the contact information at the beginning of this notice.

Legitimate interests — Where personal data is processed based on our legitimate interests, it is to improve our service and security and prevent fraud or illegal activity in favour of the wellbeing of our customers, employees, and shareholders.

## 7. Direct Marketing

We may send you information about services, courses, or events that are similar to those you have previously enquired about or purchased from us. We may also send marketing communications where you have chosen to subscribe to our mailing list.

We send such communications on the basis of legitimate interests or consent, as appropriate under applicable data protection law.

You can opt out of receiving marketing communications at any time by:

- clicking the unsubscribe link included in our emails; or

- contacting us using the details set out in this Privacy Policy.

Opting out of marketing communications will not affect your access to purchased products or services.

We do not sell personal data and we do not share personal data with third parties for their own marketing purposes.

## 8. Who We Share Your Personal Data With

We may share personal data with third parties only where necessary for the purposes described in this Privacy Policy, and only where appropriate safeguards are in place.

Depending on the nature of your interaction with Achology, this may include sharing personal data with:

Group and joint controllers — Including Kain Ramsay Limited, where relevant to providing access to courses, events, or related educational services.

Payment and financial service providers — Including accountants and payment service providers, for the purposes of processing payments, managing accounts, and complying with financial and tax obligations.

Service providers and contractors — Including associates, contractors, and suppliers who provide services on our behalf, such as marketing support, IT services, business administration, and technical support. These parties process personal data only under our instructions and are subject to appropriate confidentiality and data protection obligations.

Professional advisers — Including lawyers, accountants, auditors, and other professional advisers where necessary for legal, regulatory, or business purposes.

Technology and cloud service providers — Including software providers and cloud-based hosting or storage services used to operate and secure our platforms and systems.

Fraud prevention and security services — Including fraud detection agencies and security providers, where necessary to prevent misuse, fraud, or unauthorised access.

Public authorities and regulators — Including law enforcement agencies, courts, and regulatory bodies (such as HMRC), where disclosure is required or reasonably necessary to comply with legal obligations or to prevent or detect crime.

Business transfers — Selected third parties in connection with a proposed or actual sale, transfer, merger, or restructuring of part or all of our business, where personal data may be transferred as part of that transaction and subject to appropriate safeguards.

## 9. Joining Our Community and Attending Online Events — Information Sharing

When you register as a member of the Achology community, certain profile information will be visible to other members. You control how much information you choose to include in your profile and are responsible for managing your privacy settings in line with your preferences.

Some Achology courses and events are recorded to enable future access or viewing. Where you attend a virtual event, your name, image, or audio may be visible to other participants and, where recordings are made, to those who view the recording later. Where platform settings allow, you may be able to adjust how your name appears or anonymise your participation.

If you choose to collect or process personal data relating to other attendees or community members — for example through chat functions, direct messages, or contact exchanges — you do so independently and are responsible for ensuring compliance with applicable data protection and electronic communications laws, including UK GDPR and the Privacy and Electronic Communications Regulations (PECR). Achology does not control or assume responsibility for such processing.

Please be aware that community forums, articles, blog posts, comments, and other content you upload may be visible to other community members. You are responsible for the personal data you choose to share within these spaces.

## 10. International Data Transfers

Achology is based in the United Kingdom and primarily processes personal data within the UK. However, some of the third-party service providers we use — such as cloud hosting, software, and technical support providers — may be located outside the UK or may process personal data in other jurisdictions.

Where personal data is transferred outside the UK, we ensure that appropriate safeguards are in place to protect your data in accordance with UK GDPR. These safeguards may include:

- transfers to countries that have been recognised by the UK as providing an adequate level of data protection; or

- the use of approved contractual safeguards, such as International Data Transfer Agreements (IDTAs) or standard contractual clauses, together with appropriate additional measures where required.

We do not transfer personal data internationally unless it is necessary for the operation of our services and appropriate protections are in place.

## 11. Automated Decision-Making and Profiling

Achology does not use personal data for automated decision-making or profiling that produces legal effects or similarly significant impacts on individuals, as defined under UK GDPR.

Any decisions relating to access, participation, or services are made with appropriate human involvement.

## 12. How Long We Keep Personal Data

We retain personal data only for as long as is necessary to fulfil the purposes for which it was collected and processed, and in accordance with applicable legal and regulatory requirements.

Achology maintains an internal data retention and deletion policy that sets out retention periods for different categories of personal data. Retention periods vary depending on the nature of the data, the purpose for which it is processed, and any legal, contractual, or regulatory obligations that apply.

Personal data is not retained indefinitely. Where data is no longer required for the purposes set out in this Privacy Policy, it will be securely deleted or anonymised in line with our retention and deletion procedures, unless continued retention is required by law.

## 13. Criteria Used to Determine Retention Periods

When determining how long personal data should be retained, Achology considers the following factors:

Contractual requirements — Whether the personal data is required to perform or manage a contract with you, including providing access to courses, subscriptions, certifications, events, or support services.

Legal and regulatory obligations — Whether retention is necessary to comply with legal, regulatory, tax, accounting, audit, or reporting requirements.

Legitimate business needs — Whether retention is reasonably necessary for the operation, security, administration, or improvement of our services, including internal record-keeping and audit purposes.

Nature and sensitivity of the data — The type of personal data involved and the level of risk associated with its continued storage.

User relationship and activity — Whether you remain an active customer, community member, or subscriber, and the relevance of the data to that ongoing relationship.

Dispute resolution and legal claims — Whether the data may be required to establish, exercise, or defend legal claims, or in connection with anticipated or ongoing disputes.

### Our general data retention framework

Where personal data is required to continue the provision of our services, we will retain it for the duration of our contractual relationship with you and, in most cases, for up to 5 years after the end of that relationship. This allows us to maintain appropriate business records, ensure system security, meet legal and regulatory obligations, and support service improvement.

Where longer retention periods are required by statute, regulation, contractual obligation, or in connection with legal proceedings, personal data will be retained for as long as required to meet those obligations.

Once none of the above criteria apply, personal data will be securely deleted or anonymised in accordance with our data retention and deletion procedures.

## 14. Your Rights as a Data Subject

Under UK data protection law, you have certain rights in relation to your personal data. These rights apply in specific circumstances and may be subject to legal limitations or exemptions. Your rights include:

Right of access — You have the right to request confirmation of whether we process your personal data and, where we do, to request access to that data and related information. We do not usually charge for responding to access requests.

Right to rectification — You have the right to request that inaccurate personal data is corrected, or that incomplete personal data is completed.

Right to erasure — You have the right to request the deletion of your personal data in certain circumstances, for example where the data is no longer necessary for the purposes for which it was collected, or where processing is unlawful.

Right to restrict processing — You have the right to request that we restrict the processing of your personal data in certain circumstances, such as where the accuracy of the data is contested or processing is unlawful.

Right to object — You have the right to object to our processing of your personal data where we rely on legitimate interests or where data is processed for direct marketing purposes.

Right to data portability — You have the right to request that personal data you have provided to us is transferred to another organisation, or to you, where technically feasible and where processing is based on consent or contract.

Right to withdraw consent — Where we rely on consent as the lawful basis for processing, you have the right to withdraw that consent at any time. Withdrawal of consent does not affect the lawfulness of processing carried out before it was withdrawn.

Further guidance on these rights is available from the Information Commissioner’s Office.

## 15. How to Exercise Your Rights as a Data Subject

To exercise any of the rights set out above, or if you have a concern about how your personal data is handled, please contact us using the contact details provided at the beginning of this Privacy Policy. We would welcome the opportunity to address any concern directly in the first instance.

### Your right to complain

You also have the right to raise a complaint with the relevant supervisory authority if you believe that your data protection rights have been infringed. In the United Kingdom, the supervisory authority is the Information Commissioner’s Office (ICO). You can contact the ICO using the details below:

Information Commissioner’s Office Queen Elizabeth House Sibbald Walk Edinburgh EH8 8FT United Kingdom

Telephone: 0303 123 1115 Email: Scotland@ico.org.uk

## 16. Contractual Obligations and Consequences of Not Providing Personal Data

In some circumstances, the provision of personal data is required by law, such as to meet tax, employment, accounting, or other regulatory obligations. In other cases, the provision of personal data is necessary to enter into or perform a contract with you, including to deliver courses, subscriptions, certifications, or related services.

Where personal data is required for these purposes and is not provided, or where certain data protection rights are exercised (such as the right to erasure or the right to object), it may not be possible for us to enter into or continue a contractual relationship with you.

In such circumstances, this may result in:

- our inability to provide access to services or products; or

- the suspension or cancellation of a contract, where continued processing of the relevant personal data is necessary to meet legal or contractual requirements.

Any such consequences will apply only where the processing of the personal data is essential and cannot be reasonably avoided.

## 17. Cookies and Similar Technologies

When you visit our websites, we use cookies and similar technologies to ensure the site functions correctly, to improve performance and security, and to understand how our services are used. Cookies are small text files placed on your device by your browser when you visit a website.

We use cookies only where there is a lawful basis to do so, and non-essential cookies are used only where you have provided consent. Full details of the cookies we use, their purposes, and how you can manage your preferences are set out in our Cookie Policy.

You can also manage cookie settings through your browser. General information about managing cookies is available at allaboutcookies.org.

### Third-party websites and platforms

Our websites may contain links to third-party websites, or you may access Achology via social media or external platforms. When you follow these links or are redirected to another website, you are subject to that third party’s privacy and cookie practices.

Achology does not control the cookies, tracking technologies, or privacy settings used by third-party websites or platforms. You should review and manage your preferences directly with those providers in accordance with their own privacy and cookie policies.

## 18. Data Security

We implement appropriate technical and organisational measures to protect personal data against accidental or unlawful loss, destruction, misuse, unauthorised access, disclosure, or alteration.

Personal data is stored using secure, cloud-based systems and data centres with controlled and restricted access. We maintain internal policies and procedures covering areas such as physical security, access controls, authentication and password management, and monitoring of our systems. These measures are reviewed and updated as necessary to maintain an appropriate level of security.

While we take reasonable steps to protect personal data, no system can be guaranteed to be completely secure. Individuals are also responsible for keeping their account credentials confidential and for securing access to their own devices.

## 19. Changes to This Privacy Policy

We review and update this Privacy Policy from time to time to ensure it remains accurate, relevant, and compliant with applicable data protection laws. Any changes will be published on this page.

Our Terms & Conditions, Refunds Policy, this Privacy Policy, our Disclaimers, Cookie Policy, and Trust Statement work together to explain how Achology operates, how data is handled, and the responsibilities that apply when using our services. They should be read together as a single framework.

---

# Cookie Policy

**Live URL:** https://achologytest.com/policies/cookie-policy/
**Source read:** the deployed page output, supplied by `achology/policies-content/cookie-policy.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 1040 words.

## Body copy, verbatim

## Cookies on Achology.com

This Cookie Policy explains what cookies are, which cookies achology.com uses, why we use them, and how you can control them. It should be read alongside our Privacy Policy, which explains how we handle personal data more broadly.

## 1. What Cookies Are

Cookies are small text files that a website places on your device (computer, tablet, or phone) through your browser. They help a site remember things — that you’re signed in, what you consented to, or how you found the site — either for a single visit (“session cookies”) or across return visits (“persistent cookies”).

Cookies set by achology.com are “first-party cookies”. Cookies set by other companies whose tools we use — such as Google Analytics — are “third-party cookies”.

## 2. How We Use Cookies

We use cookies for two purposes only:

- To make the site work — essential functions such as security, remembering your cookie choices, and core WordPress functionality.

- To understand how the site is used — anonymous-style analytics that show us which pages people visit, how they arrive, and where they struggle, so we can improve the site.

We do not use advertising or ad-targeting cookies on achology.com, and we do not sell data collected through cookies.

## 3. The Cookies We Use

Strictly necessary cookies — these make the site work and do not require your consent:

| Cookie | Purpose | Duration |

| Cookie-consent preference | Remembers the cookie choices you made in our banner, so we don’t ask on every visit | Up to 12 months |

| WordPress session/security cookies | Core site functionality and security (set only where needed, e.g. if you log in) | Session, or as required |

Analytics cookies — set only with your consent:

| Cookie | Set by | Purpose | Duration |

| _ga | Google Analytics | Distinguishes visitors so we can count visits and traffic sources | Up to 2 years |

| _ga_* | Google Analytics | Maintains the session state for our analytics property | Up to 2 years |

We use Google Analytics 4, delivered through Google Tag Manager, to measure how the site is used — page views, how far down a page people read, and which links are clicked. This data informs how we improve our content and site. You can read how Google handles this data in Google’s Privacy Policy, and you can opt out of Google Analytics across all websites using Google’s browser opt-out tool.

## 4. Your Consent and How to Change It

Non-essential cookies (the analytics cookies above) are set only if you consent through the cookie banner shown on your first visit, as required by UK law (the Privacy and Electronic Communications Regulations and UK GDPR).

You can change your mind at any time:

- reopen the cookie settings via the link in the site footer and update your choices; or

- clear cookies in your browser, which resets your choices and re-presents the banner on your next visit.

Declining analytics cookies does not affect your ability to use the site.

## 5. Managing Cookies in Your Browser

Every major browser lets you view, block, and delete cookies through its settings. Blocking all cookies may stop parts of some websites working, but achology.com’s content remains readable without them. Strictly necessary cookies may be re-created the next time you visit, because the site cannot function without them, but analytics cookies stay off unless you consent again. Each browser publishes its own instructions:

- Safari — Apple’s guide to managing cookies in Safari (Mac, iPhone, and iPad)

- Chrome — Google’s guide to deleting and blocking cookies in Chrome

- Firefox — Mozilla’s guide to clearing cookies and site data in Firefox

- Edge — Microsoft’s guide to deleting cookies in Edge

Cookie choices are stored separately by each browser on each device, so if you read achology.com on both a laptop and a phone, you will need to set your preferences in each browser you use. Deleting cookies also signs you out of most websites and clears any saved preferences, so expect to be asked for your choices again on your next visit.

Some browsers can also send “Do Not Track” or Global Privacy Control signals to the websites you visit. There is no settled standard for how websites must respond to these signals, so achology.com does not act on them; we rely instead on the explicit choices you make in our cookie banner, which we are required by UK law to honour. If a recognised standard emerges, we will review how the site responds and update this cookie policy accordingly. General guidance on managing cookies across browsers is available at allaboutcookies.org.

## 6. Third-Party Platforms We Link To

Some parts of the Achology experience happen on other companies’ platforms, which set their own cookies under their own policies:

- Circle.io — our learning community and checkout run at community.achology.com on the Circle platform. When you visit, sign in, or buy there, Circle’s own cookies and privacy practices apply.

- Payment processing — payments at checkout are processed by Stripe through Circle; Stripe’s own cookies and privacy policy apply on payment pages.

- Email sign-up forms — our email list runs on Kit (formerly ConvertKit); their forms may set functional cookies under Kit’s privacy policy.

- Book links — some book recommendations on our Knowledge Hub link to Amazon through affiliate links. If you click one, Amazon may set cookies on its own site that credit Achology with a small commission on qualifying purchases, at no extra cost to you. Amazon’s own cookie practices apply there.

We do not control cookies set on third-party sites; manage those directly with each provider.

## 7. Changes to This Cookie Policy

We review this cookie policy when our cookie use changes — for example, if a new tool is added to the site — and publish updates on this page with a revised date.

## 8. Questions

If you have any questions about this Cookie Policy or how we use cookies:

- Email: support@achology.com

- Online: https://achology.com/enquiries/

This cookie policy should be read alongside our Privacy Policy, Terms & Conditions, and the rest of our policies at achology.com/policies/.

---

# Refund Policy

**Live URL:** https://achologytest.com/policies/refund-policy/
**Source read:** the deployed page output, supplied by `achology/policies-content/refund-policy.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 1098 words.

## Body copy, verbatim

## Our Approach to Refunds

Achology.com (“Achology”, “we”, “us”) is a fully online applied psychology training academy. We offer digital courses, course bundles, and community membership. This refund policy explains when refunds are available, when they are not, and how to request one. It should be read alongside our Terms & Conditions, Disclaimers, and Trust Statement.

Nothing in this refund policy reduces your statutory rights under UK consumer law.

## This Refund Policy at a Glance

- Courses, course bundles, and the Access All Areas Pass: a full refund if you request one within 14 days of purchase. No reason required.

- Achology Membership (community access): non-refundable once your access has started, but you can cancel at any time to stop future payments.

- Your legal rights: nothing in this policy reduces your statutory rights under UK consumer law.

## 1. Our 14-day money-back guarantee

We offer a full 14-day money-back guarantee on every product except community membership. This covers:

- individual courses

- school bundles

- the Access All Areas Pass

If you notify us within 14 days of your purchase that you wish to cancel, we will issue a full refund.

- You do not need to provide a reason.

- We will not dispute your decision.

- Any feedback you choose to give is entirely optional.

This guarantee applies once per customer per product. It does not apply to Achology Membership (see section 3), and it does not apply where your access has been withdrawn because of a breach of our Terms (see section 5).

Because our products are digital content supplied immediately, at checkout you consent to immediate access and waive the statutory 14-day cooling-off right, as explained in section 8 of our Terms & Conditions. This guarantee stands in its place: the same 14 days, with no reason needed.

## 2. Your course also includes community access that renews

When you buy a course, you also receive 3 months of complimentary Achology Membership (access to our learning community). After those 3 months, membership continues at the standard monthly rate (currently $34.50 per month) until you cancel. You can cancel at any time inside the community platform (Circle.io), which stops all future payments.

Please note: refunding a course within the 14-day period does not, by itself, cancel your membership. If you do not wish it to continue, please cancel it separately.

## 3. Community membership is non-refundable

Achology Membership gives you immediate access to member-only content, discussions, and live events. Because that access and its benefits begin at once and cannot be returned, membership is non-refundable. This applies to:

- Achology Membership, monthly and annual

- membership renewals

You can cancel at any time to stop future payments. The monthly plan is $7 for the first 30 days and then the standard monthly rate (currently $34.50 per month). The annual plan is $345 per year and renews each year unless you cancel before the renewal date.

## 4. After the 14-day period

Once the 14-day guarantee has passed, we do not offer refunds on courses, bundles, or the Access All Areas Pass for:

- a change of mind

- not enjoying a teaching style or approach

- disagreeing with an idea, perspective, or framework

- a lack of time, engagement, or motivation

- personal circumstances

- feeling you did not gain personal benefit

We are an education provider. Course content is interpretive, and different people experience it differently. Disagreeing with an idea, or finding a topic uncomfortable, is not a fault and is not grounds for a refund. Where lifetime access applies, your access remains available even if you choose to step away for a time.

## 5. Breach of our Terms

We will not issue a refund where your access is suspended or terminated because of:

- a breach of our Terms & Conditions

- unauthorised sharing or recording of content

- behaviour in our community spaces that endangers or exploits others (the boundary set out in our Trust Statement)

- misuse of the platform or learning materials

In such cases we may retain fees paid to reflect the losses caused by the breach, and no refund will be due unless required by law.

## 6. Technical and website issues

A temporary technical issue, platform outage, or access interruption does not automatically entitle you to a refund. A refund may be considered only where both of the following apply:

- your access to purchased content is suspended for 7 consecutive days or more, and

- the cause is attributable to us, rather than to your device, software, internet connection, or a failure to meet the stated system requirements.

## 7. Payment disputes

If something has gone wrong, please contact us first so that we can put it right. Raising a dispute or chargeback with your bank or card provider before contacting us can delay a resolution that we would otherwise be able to handle directly and more quickly.

## 8. How refunds are paid

- Approved refunds are returned to your original payment method.

- Refunds are made in US dollars, the currency in which you paid.

- We process refunds as promptly as possible. Please allow up to 5 business days for the funds to appear in your account before contacting us to follow up.

## 9. How to request a refund

To request a refund within the terms of this refund policy, please contact us with your order details so that we can process your request efficiently:

- Email: support@achology.com

- Online: https://achology.com/enquiries/

## 10. Refunds at our discretion

We may occasionally choose to offer a refund outside the terms of this policy as a goodwill gesture. Doing so on one occasion does not create a right to a refund in future, and does not oblige us to do the same in any other case.

## 11. Your statutory rights

Nothing in this policy reduces your statutory rights under UK consumer law. Where required by law, you may be entitled to a remedy if digital content is faulty, not as described, or not fit for purpose. These rights apply only in the circumstances set out in law and do not create an automatic right to a refund.

## 12. Final authority

All refund decisions are made in accordance with this refund policy, our Terms & Conditions, and applicable law. Nothing in this policy creates an obligation to issue a refund outside the circumstances expressly set out above, and nothing in this policy reduces your statutory rights.

This refund policy should be read alongside our Terms & Conditions, Disclaimers, and Trust Statement.

---

# Disclaimers

**Live URL:** https://achologytest.com/policies/disclaimers/
**Source read:** the deployed page output, supplied by `achology/policies-content/disclaimers.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 1216 words.

## Body copy, verbatim

## The Purpose of These Disclaimers

This Disclaimers statement explains the limits of Achology’s services and content. It exists to ensure clarity about what Achology does and does not provide, and to support responsible use of our educational materials. It should be reviewed alongside our Terms & Conditions, Trust Statement, Refunds Policy, and Privacy Policy.

## 1. Educational Purpose Only

All content provided by Achology is offered for educational and informational purposes only.

Achology is an education provider specialising in applied psychology, personal development, and reflective learning. Our courses, materials, events, discussions, and certifications are designed to support learning and understanding — not to deliver treatment, intervention, or personalised advice.

Nothing provided by Achology constitutes:

- medical advice

- psychological or psychiatric treatment

- counselling or therapy

- diagnosis of any condition

- crisis or emergency support

These disclaimers apply to every course, resource, and communication we publish.

## 2. No Therapy, Medical, or Mental Health Services

Achology does not provide healthcare, mental health, or therapeutic services.

Participation in Achology courses, community discussions, practice activities, or events does not create a therapist–client, doctor–patient, counsellor–client, or similar professional relationship.

If you require medical, psychological, or mental health support, you should seek assistance from a qualified and regulated professional or appropriate emergency services. In the UK: call 999 in an emergency, contact NHS 111 for urgent medical advice, or call Samaritans on 116 123 (free, 24 hours) if you need someone to talk to. Outside the UK, contact your local emergency services or a crisis line in your country.

## 3. Individual Responsibility for Use of Content

Achology teaches ideas, frameworks, models, and perspectives.

How you interpret, apply, or respond to what you learn is your responsibility. Achology does not monitor, supervise, or control how individuals apply educational content in their personal or professional lives.

You are responsible for:

- assessing whether content is appropriate for you

- managing your own emotional and psychological responses

- deciding how and whether to apply what you learn

- acting lawfully, ethically, and within your competence

Learning may involve challenge, disagreement, or discomfort. These experiences are part of education and do not constitute harm.

## 4. Ideological Content and Offence

Psychology and personal development involve ideological frameworks.

This means:

- ideas are open to interpretation

- reasonable people may disagree

- content may challenge existing beliefs

Achology does not accept responsibility for offence taken in response to educational content. Offence is a subjective response and does not indicate wrongdoing, harm, or fault on the part of Achology. These disclaimers make that boundary explicit.

## 5. No Guarantees or Promised Outcomes

Achology makes no guarantees regarding:

- personal change or development

- emotional outcomes

- professional competence

- career progression

- income, success, or recognition

Educational outcomes vary depending on individual effort, reflection, integrity, and application. Access to learning materials does not guarantee results.

For clarity: our 14-day money-back guarantee, set out in the Refunds Policy, is a refund promise, not an outcome promise.

Testimonials and student experiences: Reviews, testimonials, ratings, and student stories shared on our website or platforms reflect individual experiences. They are not promises of typical results, and your experience may differ.

## 6. Certification and Professional Boundaries

Achology certifications:

- reflect educational achievement within Achology’s framework only

- are not licences, statutory qualifications, or professional registrations

- do not grant legal authority to practise in regulated professions

It is your responsibility to:

- understand local laws and professional requirements

- ensure compliance with any regulatory or licensing bodies

- practise only within your competence and legal scope

Achology accepts no responsibility for how certifications are represented or used outside our educational context.

Services provided by people who have trained with us: Some Achology students go on to offer coaching, helping, or related services to others. Those services are provided independently. Achology does not employ, supervise, regulate, or vouch for practitioners who have completed our courses, and their clients are not Achology’s clients. Responsibility for any service delivered by an Achology-trained individual rests entirely with that individual.

## 7. Community and Peer-Based Learning

Achology operates collaborative learning environments that may include peer discussion, practice, feedback, or reflection.

Achology:

- does not supervise peer interactions

- does not verify the competence of community members

- does not endorse advice or feedback shared by others

Participation in community spaces and practice activities is voluntary and undertaken at your discretion. You are responsible for your boundaries and choices when engaging with others.

## 8. External Links and Third-Party Content

Achology websites, courses, or communications may include links to third-party websites, platforms, or resources.

Achology:

- does not control third-party content

- is not responsible for external privacy practices or policies

- does not endorse third-party views, services, or claims unless explicitly stated

Accessing external resources is done at your own discretion. These disclaimers cover Achology’s own content only.

## 9. Accuracy and Currency of Content

We take reasonable care to ensure our content is accurate and up to date at the time it is published. However, psychology, education, and applied practice evolve over time.

Achology does not guarantee that all content will remain current, complete, or applicable indefinitely. Content may be updated, revised, or withdrawn as part of our ongoing development.

## 10. Intended Audience and International Use

Achology’s services and content are designed for adults aged 18 and over.

Our content is produced in a United Kingdom context. Achology serves students worldwide, and it is your responsibility to consider how the laws, professional standards, and cultural context of your own country apply to your use of our content, certifications, and anything you go on to practise.

## 11. Limitation of Reliance

You agree that you do not rely on Achology content as a substitute for professional advice, diagnosis, or treatment.

Our liability to you is set out in section 12 of our Terms & Conditions; these disclaimers and that section work together. Nothing in these disclaimers limits or excludes any liability that cannot be limited or excluded under applicable law.

## 12. How These Disclaimers Fit With Others

This Disclaimers statement works together with Achology’s other policies to form a single framework governing your use of our services.

| Document | Its role in the framework |

| Terms & Conditions | Contractual mechanics |

| Refunds Policy | Financial boundaries |

| Privacy Policy | Data protection |

| Cookie Policy | Cookies and tracking |

| Trust Statement | Ethical philosophy |

| Accessibility Statement | Access commitment |

| Disclaimers (this statement) | Scope limits and reliance control |

No part of these disclaimers should be read in isolation.

## Final Position

Achology exists to educate thinking adults — not to manage inner worlds, regulate emotional states, or assume responsibility on anyone’s behalf.

This environment is intended for those seeking:

- psychological education grounded in personal responsibility and clear reasoning,

- open discussion without ideological coercion or therapeutic pretence, and

- a community that values maturity, agency, and thoughtful engagement over fragility.

If, instead, you are seeking:

- emotional caretaking,

- protection from challenging ideas, or

- external responsibility for internal states,

Achology is unlikely to be the right environment for you.

Recognising that boundary is not a failure — it is an expression of discernment and self-respect.

---

# Trust Statement

**Live URL:** https://achologytest.com/policies/trust-statement/
**Source read:** the deployed page output, supplied by `achology/policies-content/trust-statement.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 1122 words.

## Body copy, verbatim

## What This Trust Statement Covers

At Achology, trust begins with clarity. We are a learning organisation devoted to applied psychology, personal growth, and reflective learning. We exist to help people think clearly, understand themselves, and engage with others more responsibly.

This requires openness, reflectiveness, and intellectual maturity — qualities that cannot be developed in environments that promise comfort or protection from challenge. This trust statement explains how Achology understands individual responsibility, professional boundaries, and community-based education. It is our working philosophy, written down.

## 1. Individual Responsibility Comes First

Achology is founded on the principle that adults are fundamentally responsible for themselves.

This includes responsibility for:

- how they interpret ideas

- how they regulate their emotions

- how they manage their psychological and physiological state

- how they choose to engage, disengage, or reflect

At no point does Achology assume responsibility for managing a learner’s emotional reactions, internal responses, personal beliefs, or subjective experiences. Learning — especially learning that involves psychology, ethics, identity, values, or human behaviour — will inevitably provoke thought, disagreement, discomfort, curiosity, and insight.

These responses are not errors. They are part of learning.

Achology does not position itself as a caretaker of emotional comfort, nor as an authority over how individuals should feel. We treat our learners as autonomous adults, capable of self-regulation, reflection, and choice. That principle anchors this trust statement.

## 2. Ideological Ideas and the Right to Offence

All ideas taught at Achology are ideological in nature.

By ideological, we mean:

- they are frameworks for understanding reality, not absolute truths

- they are open to interpretation, disagreement, critique, and evolution

- they will land differently with different people, based on experience, values, culture, and temperament

For this reason, Achology — including all staff, contributors, facilitators, and management — accepts no responsibility for offence taken in response to the ideas presented within our educational materials, discussions, or community spaces.

Offence is a subjective psychological response, not an injury inflicted by instruction.

Learners are expected to:

- engage critically rather than defensively

- reflect rather than react

- step away if material is not appropriate for them at a given time

We do not dilute ideas to avoid offence, nor do we design learning to deliberately provoke it. Our responsibility is to teach honestly, responsibly, and in good faith — not to ensure uniform emotional reactions.

## 3. Emotional Self-Management Is Not Delegated

Achology explicitly affirms that each individual is responsible for managing their own emotions, reactions, and physiological state at all times. This includes responsibility for:

- stress responses

- emotional triggers

- feelings of discomfort, challenge, or disagreement

- decisions to seek additional support when needed

Achology does not provide emotional regulation, crisis management, therapy, or psychological treatment. Participation in our courses, discussions, or community does not transfer responsibility for self-care, wellbeing, or emotional regulation to the organisation or its representatives.

If a learner recognises that certain material or discussions are personally destabilising, the ethical response is to pause, seek appropriate support elsewhere (organisations such as Samaritans offer immediate, confidential help), or disengage — not to assign responsibility to an educational provider. Contact details for crisis and mental-health support are listed in our Disclaimers.

## 4. Clear Professional and Educational Boundaries

Achology is an educational institution, not a healthcare provider.

Accordingly:

- we do not diagnose, treat, or prevent mental or physical illness

- we do not provide therapy, counselling, or medical advice

- we do not replace licensed professionals or statutory services

Our certifications reflect learning, assessment, and development within Achology’s educational framework only. They do not confer legal authority, licensure, or permission to practise in regulated professions.

Learners are solely responsible for:

- understanding the legal and ethical requirements of their country

- acting within their competence

- applying what they learn responsibly, consensually, and lawfully

Education increases responsibility; it does not remove it. The full legal scope of these boundaries is set out in our Disclaimers.

## 5. Community-Based Learning and Shared Responsibility

Achology operates as a collaborative learning community. This means:

- members learn with and from one another

- discussion, practice, and reflection are central

- diverse perspectives are expected and welcomed

However, collaboration does not eliminate personal accountability. Each member remains responsible for:

- their conduct

- their language

- their boundaries

- their interpretations

While Achology moderates community spaces to uphold standards of respect and integrity, we do not assume responsibility for every interpersonal reaction, disagreement, or emotional response that may arise in group learning environments.

Community learning requires maturity. Participation is a choice.

Withdrawal of access is reserved for behaviour that genuinely endangers or exploits others: predatory conduct, harassment, or unlawful activity. That is a safety boundary, not a rulebook governing opinions or ideas. Where it must be applied, section 9 of our Terms & Conditions governs how.

## 6. Education Is Not a Guarantee

Achology makes no guarantees regarding:

- personal transformation

- emotional outcomes

- professional success

- income, status, or recognition

Learning provides tools, perspectives, and frameworks. What individuals do with those tools — and what results follow — depends on their effort, discernment, and responsibility.

Any implication that education removes personal agency or guarantees outcomes would be dishonest. We do not make such claims. This trust statement is the written record of that. Our 14-day money-back guarantee, set out in the Refunds Policy, is a refund promise, not an outcome promise.

## 7. A Relationship Built on Respect, Not Dependency

Achology’s relationship with its learners is based on mutual respect between autonomous adults.

We commit to:

- teaching honestly

- setting clear boundaries

- acting in good faith

- correcting errors when identified

In return, learners are expected to:

- take responsibility for themselves

- engage thoughtfully

- accept disagreement as part of learning

- recognise that growth often involves challenge

This is not a therapeutic container. It is a learning environment.

## Final Position

Achology exists to educate thinking adults — not to manage inner worlds, regulate emotional states, or assume responsibility on anyone’s behalf.

This environment is intended for those seeking:

- psychological education grounded in personal responsibility and clear reasoning,

- open discussion without ideological coercion or therapeutic pretence, and

- a community that values maturity, agency, and thoughtful engagement over fragility.

If, instead, you are seeking:

- emotional caretaking,

- protection from challenging ideas, or

- external responsibility for internal states,

Achology is unlikely to be the right environment for you.

Recognising that boundary is not a failure — it is an expression of discernment and self-respect.

This Trust Statement should be read alongside our Terms & Conditions, Disclaimers, and Refunds Policy, which together explain how Achology operates and the responsibilities that apply to all participants.

---

# Accessibility Statement

**Live URL:** https://achologytest.com/policies/accessibility-statement/
**Source read:** the deployed page output, supplied by `achology/policies-content/accessibility-statement.php` through `template-policy.php`. The WordPress editor for this page is empty.
**Last updated, as displayed on the page:** 1 July 2026.
**Length:** 852 words.

## Body copy, verbatim

## What This Accessibility Statement Covers

Achology.com is an online applied psychology training academy operated by Achology Transactions Ltd, trading as Achology. This accessibility statement explains our commitment to making achology.com accessible, the standard we work to, what we have built in, and how to tell us when something falls short.

## 1. Our commitment

We want everyone who visits achology.com to be able to read, navigate, and use it — including people who use a keyboard instead of a mouse, people who use screen readers or other assistive technology, people with low vision or colour blindness, and people who prefer reduced motion. Accessibility is a requirement we build to from the start, not a fix we apply afterwards. This commitment reflects our obligations to our customers under the Equality Act 2010.

## 2. The standard we work to

We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.1 at Level AA. WCAG is the internationally recognised standard for web accessibility; Level AA is the level generally accepted as the benchmark for a professionally accessible website. We also monitor the evolution of the guidelines, including WCAG 2.2, and adopt improvements as our platform develops.

## 3. What we have built in

Accessibility standards are written into our design system and applied as pages are built, including:

- Readable colour contrast. Our primary text colour exceeds the strictest WCAG contrast level (AAA) on white backgrounds, and all body-length text uses a colour combination that passes WCAG AA. Lower-contrast text is restricted to short, non-essential lines only.

- Full keyboard access. Site navigation, including dropdown menus, can be operated entirely by keyboard — menus open and close with Enter or Space, Tab moves through the links, and Escape closes a menu and returns focus to where you were.

- Screen-reader support. Navigation and interactive components carry the markup screen readers rely on to announce what a control is and whether it is open or closed, and decorative graphics are hidden from assistive technology.

- Visible focus. Every interactive element shows a clear visible outline when reached by keyboard, so you can always see where you are on the page.

- Touch-friendly interaction. Nothing on the site depends on hovering with a mouse; all functionality works by direct tap or click.

- Meaningful structure. Pages are built with semantic HTML — meaning headings, lists, and landmarks are coded as what they are, so assistive technology can navigate by structure rather than guesswork.

## 4. Conformance status

Achology.com is currently being rebuilt to the standard above. A full accessibility assessment of the finished site will be carried out as part of that rebuild, and this statement will be updated with the findings — including any known limitations and the dates by which we intend to fix them. Until that assessment is complete, we do not claim full conformance; we claim the commitment and the standards described here, and we will publish an honest account of where the site stands once it has been verified.

## 5. Known limitations

This section will list any parts of the site that do not yet meet WCAG 2.1 AA, once the post-rebuild accessibility assessment is complete. If you encounter a barrier before then, please tell us using the contact details below — reports from real use are the fastest way for us to find and fix problems.

## 6. Compatibility

Achology.com is designed to work with current versions of major browsers (Chrome, Safari, Edge, and Firefox) on desktop and mobile devices, and with commonly used assistive technologies, including screen readers, screen magnification, and speech recognition software. Course delivery and community features are provided through our learning platform (Circle.io); where a barrier arises within that platform, we will raise it with the provider and help you find a workable route in the meantime.

## 7. Tell us about an accessibility problem

If any part of achology.com is difficult or impossible for you to use, we want to know. Please contact us and describe the problem, the page you were on, and the device or assistive technology you were using:

- Email: support@achology.com

- Telephone: +44 (0)1383 344 086

- Online: our contact form

We aim to acknowledge accessibility reports within 2 working days and to tell you what we are doing about the problem. If you need any of our content in a different format, ask us and we will do what we reasonably can to provide it.

## 8. If you are not satisfied

We will always try to resolve accessibility problems directly. If you are in the United Kingdom and believe we have not responded appropriately to an accessibility concern, you can contact the Equality Advisory and Support Service (EASS), the independent service that advises on the Equality Act 2010.

## 9. About this accessibility statement

This accessibility statement was prepared on 1 July 2026 as part of the rebuild of achology.com. It will be reviewed and updated when the post-rebuild accessibility assessment is complete, and at least annually thereafter.

This accessibility statement should be read alongside our Terms & Conditions, Privacy Policy, and other policies at /policies/.
