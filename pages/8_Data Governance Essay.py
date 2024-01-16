import requests
import streamlit as st
from pathlib import Path
from PIL import Image

st.header("MSc BA: Data Governance -- A Delicate Ecosystem Which Can Easily Be Tainted")

st.subheader("Introduction")

st.write("""

Like all ecosystems, the data governance ecosystem is made up of
interdependent components that need to be balanced and maintained for
governance to work effectively. These components include hard governance
and soft governance mechanisms, policies and ethics. Societal values
underpin all these components. An analysis of each component reveals
that they have limited effectiveness on their own and therefore need to
be used in tandem to complement and reinforce each other. Ethics is a
crucial component of this ecosystem that is often overlooked or
improperly understood in data governance. The consequences of
overlooking ethics in data governance are only now being realised. The
fundamental rights of data users, like data ownership, are impacted when
ethics are not considered in data governance. InsurTech in the insurance
industry and the DPC Ireland investigation of Meta are two examples of
when data governance becomes tainted and fails.
""") 

st.subheader("Examining the Eco-System")

st.write("""

Hard governance mechanisms are legally binding rules imposed on states,
organisations and entities by a regulatory state. (Maggetti 2015). Such
regulatory states include the EU and California, and such legislations
include the General Data Protection Regulation (GDPR) and the California
Consumer Privacy Act (CCPA). Hard governance is well-defined and has
specific requirements. These mechanisms are a form of top-down
governance. The speed of innovation in data and AI technologies has
resulted in gaps in top-down governance. This phenomenon is known as the
pacing problem (Marchant 2011). As a result, governing bodies such as
the EU have played catch up in terms of enforcing hard law data
governance. For example, the Digital Services Act, which seeks to create
a safer digital environment, is one of the most recent EU legislations
entered into force in November 2022 (EC 2023). Formal top-down data
governance is therefore reactionary. This is not ideal as these
instruments can become outdated, eroding over time, and fail to adapt to
changing circumstances. One example of this is the EU's Data Protection
Directive, introduced in 1995 but not replaced until 2018 by GDPR
(Cornock 2018).

Soft governance mechanisms are another component of the data governance
ecosystem. Casanovas et al. define soft governance as guidelines,
protocols, standards, and principles that aid in governing different
groups, but they carry no legal obligation (Casanovas *et al.* 2022).
Other instruments include recommendations and informal regulatory
networks as seen in the EU (Maggetti 2015). Soft governance is more
flexible than hard governance and relies on social values and
expectations to guide behaviour instead of specific rules. To understand
soft governance instruments, it helps to look at them in the wider data
governance ecosystem. Building on Casanovas et al., I propose a Venn
diagram approach over their linear approach as a Venn diagram can better
illustrate the interactions between soft governance, hard governance,
policy and ethics.
        
""")

st.write("""


These interactions illustrate the idea that soft governance instruments
take a more holistic approach to governance, often incorporating ethical
principles or elements of hard governance. For example, soft governance
instruments that are aligned with policy and ethics are consistent with
ethical principles. One such instrument are the European Data Protection
Board (EDPB) guidelines. Many of these guidelines provide guidance on
ethical data issues, such as the application of facial recognition
technology in law enforcement (European Data Protection Board 2022).
Even for hard governance mechanisms there has been a trend towards
adopting softer forms of hard governance (Abbott and Snidal 2000).

Entities are taking more responsibility themselves in the form of
self-governance and in this way go beyond mere legal compliance. The
motivations must change to enable this form of soft governance. No
longer are pure bureaucratic forms of governance acceptable to approach
21^st^ century governance challenges, but incentive or motivation based
forms of self-governance are needed (Sørensen and Triantafillou 2016).
Acting ethically is also another motivation for organisations because
they are starting to see the consequences of not accounting for risk.
The inability to properly identify the risks data and technologies can
have on society leads to ineffective data governance. This is a problem
because as citizens we live in a digital risk society. In this society
there are three dimensions, in particular digital technologies posing
risk to users, that require new ways of theorising risks (Lupton 2016).
Ethical issues arise when these risks are not properly identified and
further complicate the governance landscape. Issues like marginalised
groups being disproportionately targeted by biased facial recognition
algorithms. One example of this is American student Amara K. Majeed
waking up to online death threats because of a mistake in a facial
recognition software that linked Majeed's picture to the name of a
suspected terrorist (Fleischer 2020). This case brings into question,
how do we effectively govern AI and ML systems?

AI ethical principles along with proper risk management must be used.
However, this is easier said than done. One major problem with soft
governance instruments is the gap between theory and practice.
Organisations have no instructions on how to operationalise principles
in specific contexts and they may be too general to apply (Whittlestone
*et al.*). The authors also note how tensions can occur during the
implementation process. One key tension is utilising algorithms while
ensuring equitable treatment. These systems have the potential to
discriminate against certain subgroups when the data is not
representative of the population (Whittlestone *et al.*). One form of
governance which could correct harmful algorithms, even in the design
stage, is ethics-based auditing (EBA) for AI. Companies can voluntarily
conduct such audits. For example, AstraZeneca conducted an EBA of their
organisational structures and processes at a high-level and detailed
audits of individual projects that develop or use AI (Mökander and
Floridi 2022). For such voluntary audits to succeed a strong
organisational culture which values ethics must also be in place.

Ethical issues also arise regarding individuals' personal data. The
right to be forgotten (RTBF), an article of GDPR states that individuals
have the right to request data controllers delete any personal data
related to them (Politou *et al.* 2018). Specifically, the ruling allows
for the removal or delisting of any URLs that appear in search results
which are associated with an EU citizen's name (Bertram *et al.* 2019).
However, there are deficiencies. Further reading shows that an
organisation's need to use someone's data may take precedence over that
person's right to have their data erased and the organisation can refuse
a request that is deemed unnecessary or unreasonable (Politou *et al.*
2018). Grey areas can arise, and the balance of power is often tipped
towards the private platforms. Delisting rates can differ from host to host.

""")      

st.write("""

As data citizens we have this privacy right, but it is not guaranteed to
be upheld. This narrative aligns with Floridi's thesis on balancing the
right to privacy with the right to freedom of expression. Floridi states
that finding this balance requires acknowledging the mistaken view that
they are always compatible (Floridi 2015). A step in resolving these
conflicts requires determining the nature of the information and
weighting up the removal on the grounds of content (availability) or the
link to the content (accessibility) (Floridi 2015). Floridi doesn't
offer in this article any practical frameworks, but ethical frameworks
or principles could help guide decisions. The principle of
nonmaleficence, the least harm principle, could be useful in guiding
decisions (Jahn 2011). To operationalise the application of this
principle, the framework of contextual integrity could be used.
Contextual integrity means protecting privacy based on the norms that
govern specific contexts. This requires that the collection and
dissemination of information aligns with the relevant context.
(Nissenbaum 2004). Specifically, Nissenbaum's contextual integrity
decision heuristic could be applied (Grodzinsky and Tavani 2011).

The complexity of online data ownership also highlights the need for
ongoing ethical discussions regarding the collection and use of
individuals' personal data. Again, ethical principles like transparency,
accountability and non-maleficence need to be operationalised by
companies and reflected in their terms and conditions. Unfortunately,
websites like Facebook profit off vague and ambiguous terms of service.
Ownership uncertainties about data are a key feature of data capitalism
as in exchange for free services, individual data is collected,
processed, and monetised without clear consent (Geiger and Gross 2021).
In the EU efforts have been made through legislation such as GDPR to
give power back to users who generate this personal data by conferring
greater ownership rights to them. An analysis of Facebook highlights the
ethical grey areas of online data ownership. In Facebook's terms of
service, they state that the user retains ownership of the IP rights of
content that is created on Facebook and Meta. However, if the user
grants permissions, then this data can be used in many ways by Facebook.
For example, if a user shares a photo, they grant Facebook permission to
share it with third-party service providers (Meta 2023). Many online
platforms operate similar policies to Facebook, meaning users own their
data but there are caveats. These caveats are where privacy and security
issues occur and in these situations these sites fail to effectively act
as data stewards. For example, Zoom while used by millions during the
Covid-19 Pandemic had poor end-to-end encryption and as a result had
access to users' video and audio data (Goodyear 2020). Zoom therefore
had too much access and control over user data. This is a clear
violation of GDPR. Under GDPR section 2 article 32, a certain level of
security proportional to the risk is required, and one of the measures
to provide security is through encryption of personal data (EUR-Lex
2016).
""")

st.subheader("Tainted Governance -- An Endemic Issue")

st.write("""
The insurance industry's use of AI and the DPC Ireland Meta
investigations highlight the reality of modern data governance.
Industries fail at data governance and the regulatory bodies responsible
for protecting data users' rights and holding companies to account can
also fail.

InsurTech integrates technologies like artificial intelligence,
blockchain, and data analytics to develop new insurance products and
services and automate processes, for example using AI in underwriting
(McFall *et al.* 2020). As this is a nascent field in insurance and
current governance has not kept pace, consumers face unintended
consequences and risks. As Kitchin points out, in exchange for the
advantages of technological innovations we face widespread data
collection and 'dataveillance' (Kitchin 2021). This axiom holds true for
the insurance industry. To make prediction models and pricing more
accurate, insurance companies rely on multiple sources of data, from big
datasets to self-generated consumer data from wearables. Personal data
harvested from these wearables is easy to monetise because permissions
are hidden in plain sight and there are grey areas as to what
constitutes permissible use of consumer data (McFall 2019). Many
insurance firms are turning to wearable health tracking devices,
companies like John Hancock and Oscar Health (Dinh-Le *et al.* 2019). It
is interesting to note that these are all American companies who are not
subject to laws like GDPR which would restrict collection of personal
data. In fact, there are no current laws preventing sensitive health
information from being collected and sold for profit in the US (Gidaris
2019). The invasiveness of this practice also begs the question, where
will the line be drawn in terms of classifying consumer behaviour risk?
Genetic data is even being gleaned by some insurers. Loopholes in US
legislation allows genetic discrimination to occur in life, disability
and long-term care insurance (Bélisle-Pipon et al. 2019).

Another proposition by some academics is that the predictions made by
insurance AI and analytics are based on biased datasets and may have
adverse effects on customers. Marginalised communities suffer as they
are singled out for higher premiums or exclusion from coverage (Lupton
2016). Many countries have anti-discrimination laws in the insurance
industry, however indirect discrimination often occurs through proxies
and opaque AI models (Xin and Huang 2022). Proxies have historically
been used in insurance pricing, but now they are being amplified by AI.
Proxies are used when AI models are deprived of personal information or
direct proxies for this information (Barry and Charpentier 2022). In
their seminal work, Schwarcz and Prince provide the example of intimate
partner violence being a proxy for charging woman higher premiums for
life or property insurance (Prince and Schwarcz 2020). Customers may not
fully know how their premium is calculated which means they are unable
to challenge any unfair or discriminatory practices.

The Data Protection Commission (DPC) Ireland shortcomings with data
governance concern how it investigated Facebook. In July 2020 the CJEU
ruled that the EU-US Privacy Shield did not provide adequate protection
for the privacy rights of EU citizens (EC 2020). Following this ruling,
the DPC Ireland was required to reinvestigate complaints against
Facebook and determine whether the company\'s transfer of personal data
to the US was legal (Tracol 2020). The DPC had not made much progress
with investigations. Since 2018, the DPC only completed two
investigations under revised GDPR (Halpin 2022). This delay led to
criticisms of the DPC by the European Data Protection Board (EDPB). The
EDPB questioned the thoroughness of the DPC's investigation since the
DPC did not include an assessment on how Facebook processed sensitive
data and recommended that they investigate further and make a new
decision (EDPB 2023). The DPC's ineffectiveness undermines the EU's
commitment to protecting the privacy rights of citizens and sends a
message to companies like Facebook that they can break EU data
protection laws and get away with it. It is also possible the DPC draws
out such investigations because it does not want to lose favour with big
tech companies who contribute heavily to the wealth of Ireland in terms
of corporation tax revenue. This is illustrated by the fact that the top
ten multinationals contributed 53% of the total corporation tax paid in
2021 (McCarthy 2021).

GDPR enforcement is weakened by prolonged legal disputes between large
multinational companies and national data commissioners (Oxford
Analytica 2022). EU states also differ in their enforcement of GDPR,
with some countries like Ireland taking a more lenient approach. Botta
and Wiedemann coin this problem the "regulatory dilemma" (Botta and
Wiedemann 2019). In their analysis of Italian, German and Irish data
protection rulings regarding Facebook, the authors note how the Italian
AGCM dismissed Facebook's claim that its registration terms were not
unfair because they had been approved by the Irish DPC (Botta and
Wiedemann 2019). This indicates that there is a lack of consistency in
how GDPR is enforced and that companies like Facebook exploit these
discrepancies by seeking regulatory approval in countries that have more
lenient enforcement. The regulatory dilemma poses a significant
challenge for the effective enforcement of GDPR and highlights the need
for greater coordination and cooperation among EU member states.
However, there are signs of change. Following EDBP advice to increase
the size of the fines, in January 2023, the DPC issued a final decision
to fine Meta Ireland €210 and €180 million for Facebook and Instagram
breaches respectively (DPC 2023).
""")

st.subheader("Conclusion")

st.write("""

Further research should focus on the development of more proactive and
practical governance frameworks for data and AI technologies, with a
particular emphasis on the implementation of ethics-based auditing. The
EU could sponsor the creation of EBA support networks that would work
with individual organisations to design frameworks which fit in with
their business models and data needs. Further research could also be
conducted on applying Nissenbaum's contextual integrity framework to
right to be forgotten requests. Further research is needed to address
the regulatory dilemma and promote consistency in GDPR enforcement
across EU member states, as well as commercial applications that can
help companies comply with these regulations.

Transparency is key for governance to work. Industries like InsurTech
could be incentivised to make some of their algorithms more transparent
and explainable. Governments could offer tax relief or grants to
companies that meet certain standards of transparency and accountability
in their use of AI.
""")

st.subheader("Bibliography")

st.write("""

Abbott, K.W. and Snidal, D. (2000) \'Hard and Soft Law in International
Governance\', *International Organization*, 54(3), 421-456, available:
<http://dx.doi.org/10.1162/002081800551280>.

Barry, L. and Charpentier, A. (2022) *The Fairness of Machine Learning
in Insurance: New Rags for an Old Man?*

Bélisle-Pipon, J.-C., Vayena, E., Green, R.C. and Cohen, I.G. (2019)
\'Genetic Testing, Insurance Discrimination and Medical Research: What
the United States Can Learn from Peer Countries\', *Nature Medicine*,
25(8), 1198-1204, available:
<http://dx.doi.org/10.1038/s41591-019-0534-z>.

Bertram, T., Bursztein, E., Caro, S., Chao, H., Chin Feman, R.,
Fleischer, P., Gustafsson, A., Hemerly, J., Hibbert, C., Invernizzi, L.,
Kammourieh Donnelly, L., Ketover, J., Laefer, J., Nicholas, P., Niu, Y.,
Obhi, H., Price, D., Strait, A., Thomas, K. and Verney, A. (2019) \'Five
Years of the Right to be Forgotten\', in *ACM SIGSAC Conference on
Computer and Communications Security*, 2019, ACM, 959-972, available:
<http://dx.doi.org/10.1145/3319535.3354208>.

Botta, M. and Wiedemann, K. (2019) \'The Interaction of EU Competition,
Consumer, and Data Protection Law in the Digital Economy: The Regulatory
Dilemma in the Facebook Odyssey\*\', *The Antitrust Bulletin*, 64(3),
428-446, available: <http://dx.doi.org/10.1177/0003603x19863590>.

Casanovas, P., de Koker, L. and Hashmi, M. (2022) \'Law, Socio-Legal
Governance, the Internet of Things, and Industry 4.0: A
Middle-Out/Inside-Out Approach\', *Special Issue The Impact of
Artificial Intelligence on Law*, 5(1), 64-91, available:
<http://dx.doi.org/10.3390/j5010005>.

Cornock, M. (2018) \'General Data Protection Regulation (GDPR) and
Implications for Research\', *Maturitas*, 111, A1-A2, available:
<http://dx.doi.org/10.1016/j.maturitas.2018.01.017>.

Data Protection Commission (2023) *Data Protection Commission Announces
Conclusion of Two Inquiries into Meta Ireland* \[press release\],
available:
<https://www.dataprotection.ie/en/news-media/data-protection-commission-announces-conclusion-two-inquiries-meta-ireland>
\[accessed 20 Mar 2023\].

Dinh-Le, C., Chuang, R., Chokshi, S. and Mann, D. (2019) \'Wearable
Health Technology and Electronic Health Record Integration: Scoping
Review and Future Directions\', *JMIR Mhealth Uhealth*, 7(9), e12861,
available: <http://dx.doi.org/10.2196/12861>.

EUR-Lex (2016) *REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND
OF THE COUNCIL*

*of 27 April 2016*

*On the Protection of Natural Persons with Regard to the Processing of
Personal Data and on the Free Movement of Such Data, and Repealing
Directive 95/46/EC (General Data Protection Regulation)*, 679,
available:
<https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679&qid=1678802396935>
\[accessed

European Commission (2020) *EU-US Data Transfers*

*How Personal Data Transferred Between the EU and US is Protected*,
available:
<https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en>
\[accessed 19 Mar 2023\].

European Commission (2023) *The Digital Services Act Package*,
available:
<https://digital-strategy.ec.europa.eu/en/policies/digital-services-act-package>
\[accessed 05 Mar 2023\].

European Data Protection Board (2022) *Guidelines 05/2022 on the Use of
Facial Recognition Technology in the Area of Law Enforcement*1, European
Data Protection Board, available:
<https://edpb.europa.eu/our-work-tools/documents/public-consultations/2022/guidelines-052022-use-facial-recognition_en>
\[accessed 05 Mar 2023\].

European Data Protection Board (2023) *Facebook and Instagram Decisions:
"Important Impact on Use of Personal Data for Behavioural Advertising"*
\[press release\], 12 Jan 2023, available:
<https://edpb.europa.eu/news/news/2023/facebook-and-instagram-decisions-important-impact-use-personal-data-behavioural_en>
\[accessed 19 Mar 2023\].

Fleischer, R.S. (2020) \'Bias In, Bias Out: Why Legislation Placing
Requirements on the Procurement of Commercialized Facial Recognition
Technology Must Be Passed to Protect People of Color\', *Public Contract
Law Journal*, 50(1), 63-89.

Floridi, L. (2015) \'\'The Right to be Forgotten\': A Philosophical View
\', *Themenschwerpunkt: Recht und Ethik im Internet Law and Ethics on
the Internet* 23, pp. 163-179 available:
<http://dx.doi.org/10.2139/ssrn.3853478>.

Geiger, S. and Gross, N. (2021) \'A Tidal Wave of Inevitable Data?
Assetization in the Consumer Genomics Testing Industry\', *Business &
Society*, 60(3), 614-649, available:
<http://dx.doi.org/10.1177/0007650319826307>.

Gidaris, C. (2019) \'Surveillance Capitalism, Datafication, and Unwaged
Labour: The Rise of Wearable Fitness Devices and Interactive Life
Insurance\', *Surveillance and Society*, 17, 132-138, available:
<http://dx.doi.org/10.24908/ss.v17i1/2.12913>.

Goodyear, M. (2020) \'The Dark Side of Videoconferencing: The Privacy
Tribulations of Zoom and The Fragmented State of US Data Privacy Law\',
*Houston Law Review*, 10, 76.

Grodzinsky, F.S. and Tavani, H.T. (2011) \'Privacy in \"The Cloud\":
Applying Nissenbaum\'s Theory of Contextual Integrity\', *SIGCAS Comput.
Soc.*, 41(1), 38--47, available:
<http://dx.doi.org/10.1145/2095266.2095270>.

Halpin, P. (2022) *Irish regulator could halt Facebook, Instagram EU-US
data flows in May*, available:
<https://www.reuters.com/world/europe/irish-regulator-could-halt-facebook-instagram-eu-us-data-flows-may-2022-02-24/>
\[accessed 19 Mar 2023\].

Jahn, W.T. (2011) \'The 4 Basic Ethical Principles that Apply to
Forensic Activities are Respect for Autonomy, Beneficence,
Nonmaleficence, and Justice\', *Journal of Chiropractic Medicine*,
10(3), 225-226, available:
<http://dx.doi.org/10.1016/j.jcm.2011.08.004>.

Kitchin, R. (2021) *Data Lives: How Data Are Made and Shape Our World*,
Policy Press.

Lupton, D. (2016) \'Digital Risk Society\' in *Routledge Handbook of
Risk Studies* Routledge, 301-309.

Maggetti, M. (2015) \'Hard and Soft Governance\' in Lynggaard, K.,
Manners, I. and Löfgren, K., eds., *Research Methods in European Union
Studies*, London: Palgrave Macmillan UK, 252-265.

Marchant, G.E. (2011) \'Addressing the Pacing Problem\' in *The Growing
Gap Between Emerging Technologies and Legal-Ethical Oversight* Springer
Netherlands, 199-205.

McCarthy, L. (2021) *Corporation Tax -- 2021 Payments and 2020 Returns*,
Revenue.ie: Revenue, available:
<https://www.revenue.ie/en/corporate/documents/research/ct-analysis-2022.pdf>
\[accessed 19 Mar 2023\].

McFall, L. (2019) \'Personalizing Solidarity? The Role of Self-Tracking
in Health Insurance Pricing\', *Economy and Society*, 48(1), 52-76,
available: <http://dx.doi.org/10.1080/03085147.2019.1570707>.

McFall, L., Meyers, G. and Hoyweghen, I.V. (2020) \'Editorial: The
Personalisation of Insurance: Data, Behaviour and Innovation\', *Big
Data &amp; Society*, 7(2), 205395172097370, available:
<http://dx.doi.org/10.1177/2053951720973707>.

Meta (2023) *Terms of Service*, available:
<https://m.facebook.com/legal/terms> \[accessed 15 Mar 2023\].

Mökander, J. and Floridi, L. (2022) \'Operationalising AI Governance
Through Ethics-Based Auditing: An Industry Case Study\', *AI and
Ethics*, available: <http://dx.doi.org/10.1007/s43681-022-00171-7>.

Nissenbaum, H. (2004) \'Privacy as Contextual Integrity\', *Washington
Law Review*, 79, 119.

Oxford Analytica (2022) \'GDPR Enforcement Will Improve Slowly in the
EU\', *Emerald Expert Briefings*, (oxan-db), available:
<http://dx.doi.org/10.1108/OXAN-DB274294>.

Politou, E., Alepis, E. and Patsakis, C. (2018) \'Forgetting Personal
Data and Revoking Consent Under the GDPR: Challenges and Proposed
Solutions\', *Journal of Cybersecurity*, 4(1), available:
<http://dx.doi.org/10.1093/cybsec/tyy001>.

Prince, A.E. and Schwarcz, D. (2020) \'Proxy Discrimination in the Age
of Artificial Intelligence and Big Data\', *Iowa L. Rev.*, 105,
1257-1318.

Sørensen, E. and Triantafillou, P. (2016) *The Politics of
Self-Governance*, Routledge.

Tracol, X. (2020) \'"Schrems II": The Return of the Privacy Shield\',
*Computer Law & Security Review*, 39, 105484, available:
<http://dx.doi.org/https://doi.org/10.1016/j.clsr.2020.105484>.

Whittlestone, J., Nyrup, R., Alexandrova, A. and Cave, S. \'The Role and
Limits of Principles in AI Ethics\', in 2019, ACM, available:
<http://dx.doi.org/10.1145/3306618.3314289>.

Xin, X. and Huang, F. (2022) \'Anti-Discrimination Insurance Pricing:
Regulations, Fairness Criteria, and Models\', available:
<http://dx.doi.org/10.2139/ssrn.3850420>.

""")
