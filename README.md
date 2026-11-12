# Custom OpenAI AI Tasks (HA)

Home Assistant integration that plugs any **OpenAI-compatible** `/v1` server
(OpenAI, local engines, proxies) into HA's built-in **AI Task** framework —
the same mechanism the "Generative AI camera snapshot notification" blueprints
use to caption doorbell snapshots with a cloud model.

Fork of [loryanstrant/HA-Azure-AI-tasks](https://github.com/loryanstrant/HA-Azure-AI-tasks)
(v2.4.0, MIT), adapted so the OpenAI-compatible surface is the only mode:

- URL: `{server}/v1/{chat/completions|images/...}` — paste the server root
  (`http://host:8000`) or with a trailing `/v1`; both are normalised
- Auth: `Authorization: Bearer <key>` (always)
- Model name sent in the request body
- No `api-version` query parameter
- Config-flow connectivity test hits `{server}/v1/models`

## Install (HACS)

HACS → Integrations → ⋮ → Custom repositories → add
`https://github.com/benchieng/ha-openai-ai-tasks` (category **Integration**) →
install → restart HA.

Or manually: copy `custom_components/custom_openai_ai_tasks/` into your HA
config dir and restart.

## Configure

Settings → Devices & Services → Add Integration → **Custom OpenAI AI Tasks**:

- Endpoint: e.g. `http://192.168.1.79:8000`
- API key: the server's key
- Chat model: e.g. `qwen3.8-27b-vision` (free text; leave image model empty
  if the server doesn't generate images)

The resulting `ai_task.*` entity works with any blueprint/automation that
calls `ai_task.generate_data` with an `attachments:` snapshot — point the
blueprint at this entity and it stops calling the cloud model.

Requires Home Assistant 2025.10+.
