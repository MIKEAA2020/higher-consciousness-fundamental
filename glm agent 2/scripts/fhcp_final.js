// fhcp_final.js — Part II: Repairs; Part III: The Consolidated Premise (sections 9-12)
"use strict";
const { h1, h2, h3, para, quote, bullet, tableTitle, makeTable } = require("./fhcp_lib.js");

function buildFinal() {
  const c = [];

  // ─────────────────────────────────────────────────────────────
  // 9. TEN REPAIRS
  // ─────────────────────────────────────────────────────────────
  c.push(h1("9. Ten Repairs Before Consolidation"));
  c.push(para([
    { t: "The repairs below convert the audit's findings into standing rules for the consolidated premise. Each repair is labeled with the weaknesses it addresses, and each becomes part of the premise's own text in Section 10 or its apparatus in Sections 11 and 12. They are stated compactly here because the premise must be able to carry them without commentary." },
  ]));
  c.push(h2("R1. Institutionalize the two-language regime"));
  c.push(para([
    { t: "Adopt the Lexicon of Eternal Being as binding for all ontological statements, and mark every use of process vocabulary (dreaming, rendering, collapse, before, after, creation, beginning) as pedagogical upaya, explicitly discarded once the point is made. The transcript needed this rule stated once (L5479) and then still required three further corrections (C9, C12, C13); the rule works only if enforcement is lexical, not aspirational. Addresses W3, W4, and the entire correction log." },
  ]));
  c.push(h2("R2. Grade every claim and ban inflation"));
  c.push(para([
    { t: "Three grades, marked in the text itself where ambiguity would otherwise creep: physics fact (A), structural analogy (B), metaphysical interpretation (C). The words 'proof', 'smoking gun', 'vindication', 'necessity', and 'must' are reserved for Grade A uses or deleted. The single hedge that the dialogue got right becomes the default posture: 'a metaphysical interpretation, not an established scientific claim' (L1151). Addresses W1, W3, W5, W7." },
  ]));
  c.push(h2("R3. Commit to one Bell response"));
  c.push(para([
    { t: "The premise answers Bell with topological priority and holistic covariance: setting and particle are not independent because they are topologically posterior expressions of one structure, and entanglement is the non-spatial unity of that structure. The earlier narrations, sacrificing locality or realism, are retired and recorded as superseded. This gives the premise a single answer where the transcript offered three (Table 2), and it is the answer that composes with C14. Addresses W1 and the contradictions of Section 6." },
  ]));
  c.push(h2("R4. Fix the account of probability"));
  c.push(para([
    { t: "The Born rule is stated once, in the final form: the equilibrium distribution of a confined perspective, with quantum non-equilibrium as the observable signature of the unsettled condition. 'Narrative weight' and the raw axiom are retired. The account is carried at Grade B and is tied to the empirical annex, since it is the only part of the probability story with a falsifiable edge. Addresses the Born-rule contradiction and W6." },
  ]));
  c.push(h2("R5. Maintain an honest empirical ledger"));
  c.push(para([
    { t: "Exactly three items belong on it: Valentini-type non-equilibrium signatures in the cosmic microwave background; objective-collapse parameter windows; and the classical-AI consciousness ceiling with the associated quantum-computing complexity wall. Each is listed with what it would establish, what it would not, and which rival programs predict the same outcomes. The ledger also records the framework's own owed criteria, the hidden variables, the probability measure, the quantitative reproduction, the no-signaling guarantee, and the predicted deviations (L1554-1562). No other empirical claim is permitted to carry weight. Addresses W1, W5, W8." },
  ]));
  c.push(h2("R6. State the free-energy inversion as a wager"));
  c.push(para([
    { t: "The Markov-blanket and free-energy formalization is stated as the premise's central wager about where the law of dissociation will come from, not as a feasibility transfer from physicalist neuroscience. The physicalist reading of the same mathematics remains available, and the premise says so. Decombination is carried as the premise's largest open problem, exactly as the external critique demanded (L3879-3891). Addresses W2, W12." },
  ]));
  c.push(h2("R7. Engage the rivals"));
  c.push(para([
    { t: "The consolidated premise names its nearest alternatives, Russellian monism and panpsychism, which share the intrinsic-nature diagnosis at lower ontological cost, and the semantic-externalist tradition, which blunts dream and simulation arguments by observing that dream-talk refers inside the dream. The premise's answer to the first rivals is the unity of experience and the parsimony argument the transcript states best at L7748, one substance rather than two, offered as a reason rather than a proof. The answer to the second is that the premise's claim is ontological, not skeptical: it does not doubt the world's reality; it reinterprets its substance, in the spirit of Chalmers's second form of the dream hypothesis (L7732-7740). Addresses W11." },
  ]));
  c.push(h2("R8. Strengthen the theodicy, honestly"));
  c.push(para([
    { t: "The premise keeps totality and play as its account of suffering and adds the admission the transcript omitted: the account's cost is borne by the avatars, and the premise has no argument that forces acceptance, only the testimony that contrast is the condition of experience. It is stated as the premise's moral remainder, not resolved. Addresses W10." },
  ]));
  c.push(h2("R9. Downgrade the demonstrations"));
  c.push(para([
    { t: "The infinity, mirror, and completeness arguments for the necessity of avatars are retained as reasons internal to the premise's own commitments, with their counters named: infinity need not instantiate every perspective experientially; consciousness may not require subject-object structure; the keystone claim of structural dependence is asserted, not derived. Nothing in the premise's core now depends on their validity. Addresses W9." },
  ]));
  c.push(h2("R10. Declare the register"));
  c.push(para([
    { t: "The consolidated premise is a metaphysical interpretation that maintains an empirical annex. The interpretation earns its keep by unification and parsimony; the annex tests the boundary story and keeps the premise honest; neither masquerades as the other. This single declaration dissolves the awkwardness of the transcript's ending, in which a laboratory program and a timeless Singularity coexist without a stated relation (W12). It also honors the dialogue's own best self-description, 'a coherent bet', now made structural." },
  ]));

  // ─────────────────────────────────────────────────────────────
  // 10. THE CONSOLIDATED PREMISE
  // ─────────────────────────────────────────────────────────────
  c.push(h1("10. The Consolidated Premise (Final Form)"));
  c.push(para([
    { t: "What follows is the premise itself, restated in your voice, incorporating the fourteen corrections and the ten repairs. It uses the two-language regime: ontological statements are made in the language of eternal being; process language appears only where flagged as pedagogical. It is organized as a credo, a doctrine of layers, a doctrine of time, a doctrine of ground, and an honest status clause." },
  ]));

  c.push(h2("10.1 The credo"));
  c.push(quote(
    "There is no individual me; that is another avatar construct, starting from birth and ending with death. God did not create a universe. God is all there is. That is the objective, unchanging reality. What we are experiencing as the universe is a subjective perspective of the unchanging God. The apparent creation is a necessity of objective, perfect, complete truth, not some separate extension or creation. There is only one, whole, unchanging truth.",
    "(your words, L9673-9675)"));
  c.push(para([
    { t: "I hold that the ultimate, objective truth, which the traditions call God and which this premise calls the Absolute or the Singularity, is timeless, spaceless, unchanging, and without parts or composites (L10911, L10918). It does not dream, simulate, or create in time; those are verbs of process, and process belongs to the perspective, not to the ground (L5307-5318). It does not undergo change, has no before or after, and nothing stands outside it (L5330-5337). The physical universe is not a separate object beside it but its extrinsic appearance: the eternal, static, necessary geometry of the Infinite as viewed from finitude (L5364-5368). I am not a created being inside this appearance; I am one of its localized perspectives, an avatar whose boundaries begin at birth and end at death and whose individuality is itself part of what appears (L9673). Where the credo speaks of a dream, of rendering, or of creation, I use those words as pedagogical instruments only, to be discarded once the point is made; this is the discipline I adopt from the dialogue's own corrections, and I apply it to my own formulations hereafter." },
  ]));

  c.push(h2("10.2 The doctrine of layers"));
  c.push(para([
    { t: "The premise is stratified. It distinguishes the unmanifest Absolute, beyond mathematics and description, from its eternal mathematical expression, the Logos, and from the rendered order that you and I inhabit. The wavefunction of physics, the nets of algebra in algebraic quantum field theory, and twistor geometry are read as dialects of the Logos, not as the Singularity itself: the wavefunction is the nomological structure of the manifold, discoverable but not subjective (L5827-5838). Between the Logos and the appearance stands what the dialogue called the tether: the atemporal consistency constraints that make the local everywhere covary with the whole, for which topological priority is the governing concept (L11039-11059). Within the appearance, the rendering threshold of objective collapse, the consensus protocol of Quantum Darwinism, and the avatar's epistemic horizon each do their work at their own stratum. Table 5 states the layers with their physics correspondences, each correspondence held at the grade the audit assigned it." },
  ]));
  c.push(tableTitle("Table 5. The stratified ontology (consolidated)"));
  c.push(makeTable(
    ["Layer", "Ontological role", "Physics correspondence", "Grade"],
    [
      ["The Absolute (Singularity)", "The unmanifest, non-composite ground; pure actuality; beyond mathematics.",
       "None by definition; approached negatively.", "C"],
      ["The Logos", "The eternal, spaceless mathematical expression of the Absolute; the global blueprint.",
       "Universal wavefunction; global state on the C*-algebra; twistor space; configuration space.", "B"],
      ["The tether", "Atemporal consistency: the part cannot contradict the whole; topological priority.",
       "Guidance equation; GNS construction; incidence relation; transactional handshake.", "B"],
      ["The rendering threshold", "Where unbounded potential is restricted into definite, classical appearance.",
       "Objective collapse (GRW, CSL, Penrose); decoherence as interface.", "B"],
      ["The consensus protocol", "Redundant broadcasting that makes appearance shared and stable.",
       "Quantum Darwinism; environmental redundancy.", "A/B"],
      ["The avatar's horizon", "The localized perspective: memory, agency, sequence; the arrow lives here.",
       "Relational QM; QBism; the perspectival reading of the partial trace.", "B/C"],
    ],
    [19, 33, 34, 14],
    { zebra: true, size: 19 }
  ));

  c.push(h2("10.3 The doctrine of time"));
  c.push(para([
    { t: "Time is not one thing, and the reconciliation of quantum mechanics and general relativity that the premise offers is the stratified one the dialogue converged on (L7050-7067). At the level of the Absolute there is no time: no sequence, no before, no after (L3089-3092). At the level of the manifold, time is a static geometric coordinate, and general relativity is the physics of its curvature (L3094-3099). At the level of the avatar, time is lived sequence, and the parameter of the Schrodinger equation is the internal clock of a perspective that cannot take in the whole at once (L7017-7023). The Wheeler-DeWitt equation, read as the signature of the timeless level, is a Grade B correspondence the premise keeps with its hedge attached. The arrow of time is the direction of actualization: the past is the settled record, the future the open potential, the present the edge where records are written (L2201-2207). The low-entropy boundary we call the Big Bang is the local horizon of this perspective, not the beginning of anything absolute (L2331-2336); 'beginning' and 'initial' are process words, and I use them only pedagogically. I retain the honest limit of this doctrine: a measure for typicality, including the Boltzmann-brain question, is still owed (L1903)." },
  ]));

  c.push(h2("10.4 The doctrine of ground: topological priority"));
  c.push(para([
    { t: "The premise replaces causation at the fundamental level with topological priority (L11028-11086). The boundary is prior to the bulk as the canvas is prior to the painting and the axioms to the theorems; nothing happens first and nothing is pushed later. The correlations that science reads as causation are entailments: the neural correlate and the conscious state are one structure viewed from two sides, and the measurement setting and the particle's state are parts of one global invariant (L10979-11015). This is the premise's single answer to Bell: statistical independence fails because separateness itself is derivative, and entanglement is the non-spatial unity of the Logos showing through (L5154-5167). Physical causal closure is preserved, since nothing mental interrupts the appearance's order; downward causation is replaced by vertical grounding (L9228-9278). Emergence, correctly interpreted, is a change of perspective or layer, not a process (L9154-9181); what physics calls the emergence of spacetime the premise calls its grounding in entanglement, with the Ryu-Takayanagi relation carried as the strongest Grade B witness (L6964-6971)." },
  ]));

  c.push(h2("10.5 The doctrine of the person"));
  c.push(para([
    { t: "I am a topological boundary, a Markov blanket, in the metaphor of the borrowed mathematics: a localized, self-maintaining horizon through which the Absolute appears to itself as finite (L3962-3963). The brain is not my generator; it is the extrinsic image of my boundary (L2794-2804). The individual 'me' is a rendered construct, a narrative subroutine bounded by birth and death (L9686-9691); its deliberation is real at its layer and its freedom is the freedom of what it ultimately is, not of the construct (L8790-8817). Other avatars are not solitons of private worlds: consensus through redundant broadcasting is what objectivity means, and the moon is there when nobody looks in the sense that its pointer states are multiply recorded in the shared environment (L3597-3608). The arguments that such avatars are necessary features of the Absolute I keep as reasons, not demonstrations: infinity and completeness suggest the inclusion of finitude, self-knowledge suggests a mirror, and play and love suggest why the inclusion is not a defect (L9535-9604, with W9's counters named)." },
  ]));

  c.push(h2("10.6 The honest status clause"));
  c.push(para([
    { t: "This premise is a metaphysical interpretation with an empirical annex, and I state its condition in the dialogue's own best words: it is 'a coherent bet, not a guaranteed answer' (L3893). It earns consideration by unification, one substance rather than two (L7748), by dissolving the hard problem without magic, and by making the physics I trust hang together with the experience I cannot doubt. It does not yet explain the data better than physicalism; it accommodates them (L3873). Its largest open problem is decombination, the law by which the one becomes many, and the Markov-blanket program is my wager on where that law will be found, a wager stated as such and not as a feasibility transfer (R6). Its moral remainder is the suffering of avatars, which totality and play illuminate but do not justify (R8). It faces rivals it must continue to answer: Russellian monism and panpsychism to one side, semantic externalism to the other (R7). And it keeps a small ledger of claims the world could wound, not because the Absolute could be falsified by appearances, but because the boundary story, which is the part of the premise that lives at the interface, can be (Section 11). Until its Newton arrives, I hold it the way one holds a conviction that knows itself: firmly, transparently, and ready to be corrected again." },
  ]));

  // ─────────────────────────────────────────────────────────────
  // 11. EMPIRICAL ANNEX
  // ─────────────────────────────────────────────────────────────
  c.push(h1("11. Empirical Annex: The Falsifiable Edge of the Premise"));
  c.push(para([
    { t: "The annex lists everything in the premise's orbit that experiments can touch. Its rules are the audit's: each item records what a result would establish for the boundary story, what it would not establish for the Absolute, and which rival programs expect the same result. The annex also carries the criteria the dialogue itself conceded it owed: a precise ontology, a law of dissociation, a brain-to-experience mapping, novel predictions, and an account of the lawlike world (L3879-3883). Items on the ledger are the only empirical claims the premise is permitted to advance." },
  ]));
  c.push(tableTitle("Table 6. The empirical ledger"));
  c.push(makeTable(
    ["Test", "Positive result would establish", "Would not establish", "Shared with"],
    [
      ["Valentini-type quantum non-equilibrium in the cosmic microwave background or relic particles (L10091-10098).",
       "The Born rule is an equilibrium, not an axiom; probability is perspectival; the premise's account of probability gains Grade A support.",
       "The idealist substrate; deterministic subquantum theories suffice for the physics.",
       "De Broglie-Bohm and superdeterminist programs; some quantum-gravity phenomenology."],
      ["Objective-collapse parameter windows (GRW, CSL, Penrose-Diosi) probed by optomechanics and interferometry (L6155-6167).",
       "A physical rendering threshold at Layer 3 exists, as the stratified ontology assigns.",
       "Any interpretation of the threshold as experiential; collapse theories are physics-first.",
       "Objective-collapse research program; independent of idealism."],
      ["Classical-AI consciousness ceiling and the quantum-computing complexity wall (L3931-3939; L3331-3336).",
       "The boundary story's claim that consciousness is not substrate-independent classical computation.",
       "The Absolute; even a ceiling is consistent with non-idealist biological naturalism.",
       "Penrose-Hameroff program; skeptics of strong AI consciousness."],
    ],
    [22, 30, 26, 22],
    { zebra: true, size: 19 }
  ));
  c.push(para([
    { t: "Two annex disciplines complete the ledger. First, the negative space is recorded with the same care as the positive: if quantum non-equilibrium is never found and constrained ever tighter, the equilibrium account of the Born rule weakens toward metaphor, and the premise must say so rather than absorb the null result as confirmation (W1's lesson). Second, the encoding-model program for the functor R is retained as method, not as discriminator: mapping neural manifolds to experiential proxies with topological data analysis (L4110-4175) is good science under either ontology, and the premise claims from it only what a physicalist identity theory would also claim, structural isomorphism, leaving the direction of grounding to interpretation (W8's lesson)." },
  ]));

  // ─────────────────────────────────────────────────────────────
  // 12. GLOSSARY
  // ─────────────────────────────────────────────────────────────
  c.push(h1("12. Glossary of the Final Vocabulary"));
  c.push(para([
    { t: "The glossary enforces the two-language regime (R1). Table 7 defines the ontological vocabulary in which the premise is stated. Table 8 lists the process vocabulary permitted only as pedagogy, each entry with its sanctioned pedagogical use and its standing prohibition. The line ranges give where each term was fixed in the transcript, at its latest corrected occurrence." },
  ]));
  c.push(tableTitle("Table 7. Ontological vocabulary (the language of eternal being)"));
  c.push(makeTable(
    ["Term", "Definition", "Fixed at"],
    [
      ["The Absolute / the Singularity", "The one, timeless, spaceless, non-composite reality; pure actuality; all there is. Not an object among objects, and not made of parts, bits, or quanta.", "L5307-5372; L10911-10963"],
      ["The Logos", "The eternal, spaceless mathematical expression of the Absolute; the global structure that physics approaches through wavefunction, algebra, and geometry. Distinct from the Singularity, which is beyond mathematics.", "L5827-5838; L5930-5947"],
      ["The extrinsic manifold", "The physical universe understood as the static, four-dimensional appearance of the Absolute to finite perspective; the rendered order.", "L5497; L5559-5597"],
      ["Topological priority", "The structural precedence of ground over grounded: boundary over bulk, canvas over painting. The replacement for temporal causation at the fundamental level.", "L11028-11086"],
      ["Holistic covariance", "The atemporal consistency of the whole: parts cannot be statistically independent because separateness is derivative. The premise's settled Bell response.", "L6048-6051; L8727-8742"],
      ["Perspectival actualization", "The process-by-appearance in which a finite perspective converts open potential into settled record; the home of the arrow of time.", "L1859-1873; L3152-3158"],
      ["The Markov blanket", "The localized, self-maintaining boundary of an avatar; borrowed from statistical structure as the premise's wager on the shape of the law of dissociation.", "L3962-3963; L8975-8984"],
      ["Quantum equilibrium", "The settled condition of a confined perspective in which the Born rule holds; its violation, non-equilibrium, is the annex's principal observable.", "L9988-10048"],
    ],
    [22, 56, 22],
    { zebra: true, size: 19 }
  ));
  c.push(tableTitle("Table 8. Pedagogical vocabulary (upaya; use and discard)"));
  c.push(makeTable(
    ["Term", "Sanctioned pedagogical use", "Standing prohibition"],
    [
      ["Dream / dreaming", "To convey that the universe is appearance within mind, as in Chalmers's second form: the objects exist, but their substance is mental.", "Never as event or change of state; the Absolute does not begin or cease dreaming (C4)."],
      ["Rendering / collapse", "To convey the restriction of potential into definite appearance at the avatar's horizon.", "Never as a process undergone by the Absolute; collapse is perspectival, not global (Table 2)."],
      ["Creation / creator", "To introduce the premise to theistic audiences by contrast.", "Never ontologically: there is no maker, no made, and no outside (L9692-9699)."],
      ["Before / after / beginning", "To order exposition for time-bound readers.", "Never about the Absolute or the manifold as such; the Big Bang is a boundary, not an event (C7, C8)."],
      ["Boot-up / compilation / patching", "To borrow intuitions from computing when explaining cosmology.", "Never literal; flagged as simulation-hypothesis residue and dropped immediately (C3, C9)."],
      ["Defect / glitch / error", "To describe how anomalies appear to avatars.", "Never about the Absolute, which is perfect; defects are avatar constructs (C2)."],
    ],
    [20, 40, 40],
    { zebra: true, size: 19 }
  ));
  c.push(para([
    { t: "The glossary closes the consolidation where the dialogue itself closed: with vocabulary made obedient to the position it serves. The premise's claims are now graded, its Bell response is single, its probability account is fixed, its ledger is honest, its rivals are named, its suffering is carried rather than explained away, and its process language is flagged at every use. What remains is exactly what the transcript's best sentence promised and its best moments delivered: a coherent bet, held openly, about the one unchanging truth in which all of this, including this audit, appears." },
  ]));

  return c;
}

module.exports = { buildFinal };
