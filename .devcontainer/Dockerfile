# Use Debian sid for latest Python 3.14 packages
# But you can switch to a stable release if you prefer
FROM debian:sid-slim AS base 

ARG PYTHON_VERSION=3.14.0
ARG USERNAME=appuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG WORKDIR=/devcontainer

WORKDIR $WORKDIR

# Install build dependencies and compile Python from source
# You can add additional dependencies here if your project requires them
RUN apt-get update && apt-get install -y --no-install-recommends \
  git curl build-essential \
  ca-certificates pkg-config \
  python3.14 python3.14-venv python3.14-dev \
  && ln -s /usr/bin/python3.14 /usr/local/bin/python

RUN useradd -m -u $USER_UID -s /bin/sh $USERNAME && chown -R $USERNAME $WORKDIR

# Install zsh and set it as default shell
RUN apt-get update && apt-get install -y --no-install-recommends \
  zsh \
  && rm -rf /var/lib/apt/lists/* \
  && chsh -s /bin/zsh $USERNAME

# Install Oh My Zsh for appuser
USER $USERNAME
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install Powerlevel10k theme
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-/home/$USERNAME/.oh-my-zsh/custom}/themes/powerlevel10k \
  && sed -i 's|ZSH_THEME="robbyrussell"|ZSH_THEME="powerlevel10k/powerlevel10k"|' /home/$USERNAME/.zshrc

# Copy p10k config and source it from .zshrc
COPY --chown=$USERNAME .p10k.zsh /home/$USERNAME/.p10k.zsh
RUN echo '[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh' >> /home/$USERNAME/.zshrc

# You can configure here for example:
# - git
# - gcloud
# - kubectl, k9s
# - nnn
# - etc.

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONUNBUFFERED=1 \ 
  POETRY_NO_INTERACTION=1 \
  POETRY_VERSION=2.3.2

RUN python -m venv $WORKDIR/.venv
RUN chown -R $USER_UID:$USER_GID $WORKDIR/.venv

ENV PATH="$WORKDIR/.venv/bin:$PATH"

RUN pip install "poetry==$POETRY_VERSION"

SHELL [ "/bin/zsh", "-c" ]