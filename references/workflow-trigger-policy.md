# Workflow Trigger Policy

The transcript-to-blog workflow should only be triggered when a **new task explicitly includes a transcript or transcript-derived source material**.

Accepted trigger inputs:

- raw transcript
- call transcript
- meeting transcript
- transcript summary with supporting excerpts
- bundled transcript-derived source package

Do not trigger the workflow when:

- the user asks for a general blog idea without source material
- the task is only a content strategy discussion
- there is no transcript evidence included
