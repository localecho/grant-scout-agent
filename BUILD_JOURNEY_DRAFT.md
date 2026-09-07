# builder.aws.com post draft — bonus points track

Title must include "Agents for Humans" per the rules. Publish before the Sep 14, 2026 5pm PDT
deadline. This is a draft to edit and post on builder.aws.com, not the final published copy.

---

## Title

**Agents for Humans: catching a grant that sounds right but isn't, with a two-tool Strands agent**

## Body

Small nonprofits — food banks, libraries, community programs — don't lose grant money because
writing applications is hard. They lose it because finding the *few* opportunities they can
actually win, out of tens of thousands of live listings, takes hours most volunteer boards
don't have. For AWS's Agents for Humans Hackathon, I built **Grant Scout**, a Strands agent
that runs that search-and-vet loop and only surfaces a short list worth a human's five minutes.

**The design decision that mattered most wasn't the search tool — it was the second one.**
Grant program titles lie by omission. A program literally named "Cold Chain Grants for
Emergency Food Assistance" reads as a perfect match for a food pantry. It's the kind of result
a naive agent would confidently recommend. Grant Scout's second tool,
`historical_award_context`, checks that claim against a real table derived from
USASpending.gov's public bulk award data — and for that specific program, there's no verified
501(c)(3) nonprofit award history at all in FY2021. The agent's system prompt tells it to treat
that absence as a real risk signal, not a false negative to ignore, and to say so explicitly in
its output rather than quietly recommending anyway.

That's the pattern I'd generalize from this build: when an agent is making an eligibility or
fit claim that a human will act on, ground it against a second, independent, real data source —
not just the first search result's own framing of itself.

**On Strands specifically:** the provider-agnostic model interface meant I could build and
iterate against OpenRouter (fast, one key, easy model swapping while I found tool-calling
issues) and then flip to Amazon Bedrock with the same agent code and one environment variable —
`src/agent.py`'s `_build_model` function is the whole diff. That's not a hack around AWS's
stack; it's Strands doing exactly what a model-provider abstraction is supposed to do.

Repo (MIT licensed): `<REPO_URL>`

#AgentsForHumans #StrandsAgents #AWS
