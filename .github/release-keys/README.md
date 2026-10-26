<!--
SPDX-FileCopyrightText: 2026 Eng. Hamada Sami
SPDX-License-Identifier: Apache-2.0
-->
# Release signer keys

This directory holds the ASCII-armoured OpenPGP **public** keys (`*.asc`) of the
VCGF release maintainers who are allowed to sign release tags. The
`Draft release for a signed tag` workflow (`.github/workflows/release.yml`)
imports every `*.asc` file found here into an empty keyring and then runs
`git tag -v <tag>`, so a tag is accepted only when it carries a valid signature
from one of these keys.

## Current state

- **No signer keys are committed yet.** Until a maintainer adds a key here, the
  release workflow fails at the "Import allowed signer keys" step by design and
  no release draft can be produced.
- A release cannot be drafted until a maintainer adds a key **and** an
  independent reviewer confirms the key fingerprint in the pull request that
  introduces it. The reviewer must verify the fingerprint through a channel
  other than the pull request itself (for example a signed message or a direct
  conversation with the key owner) and state the confirmed fingerprint in the
  review.

## Adding a key

1. Export the public key only: `gpg --armor --export <FINGERPRINT> > .github/release-keys/<github-handle>.asc`.
2. Open a pull request that adds the file and names the full 40-character
   fingerprint in its description.
3. An independent reviewer confirms the fingerprint as described above before
   the pull request is merged. Never commit a private key or a key without a
   confirmed fingerprint.

## Signing tags

Release tags must be created as signed annotated tags, for example
`git tag -s v1.3.1 -m "VCGF v1.3.1"`, with the signing key listed here. The
release workflow never creates or moves tags; it only drafts a release for an
already signed tag, and publishing the draft remains a manual action after
independent review.
